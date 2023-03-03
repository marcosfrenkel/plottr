import time
from pathlib import Path
from typing import Union, Optional, Dict, List, Tuple

from .node import Node, updateOption, NodeWidget
from ..data.datadict import DataDictBase, datadict_to_meshgrid, _mesh_mean
from ..data.datadict_storage import datadict_from_hdf5


# TODO: There should be a child class that can do histogramming
# TODO: should run on a separate thread to not hung the UI
# TODO: Further improvements are also needed.
class AverageLoader(Node):
    """
    Loader that can average over specified axis since loading
    """

    nodeName = 'AverageLoader'
    useUi = None

    def __init__(self, name: str):
        super().__init__(name)

        self._filepath: Optional[Path] = None
        self._groupname: str = 'data'
        self._average_axes: List[str] = []

        self.nLoadedRecords = 0
        self.startTime: Optional[float] = None

    @property
    def filepath(self) -> Path:
        return self._filepath

    @filepath.setter
    def filepath(self, path: Union[str, Path]) -> None:
        path = Path(path)
        self._filepath = path

    @property
    def groupname(self) -> str:
        return self._groupname

    @groupname.setter
    def groupname(self, val: str):
        self._groupname = val

    @property
    def average_axes(self) -> List[str]:
        return self._average_axes

    @average_axes.setter
    def average_axes(self, val: Union[List[str], str]):
        """
        You can set this as a single string and the function will convert it to a list
        """
        if isinstance(val, str):
            val = [val]
        self._average_axes = val

    def process(self, dataIn: Optional[DataDictBase]=None) -> Optional[Dict[str, Optional[DataDictBase]]]:

        self.startTime = time.time()

        if self._filepath is None or self._groupname is None:
            return None

        data = datadict_from_hdf5(self._filepath, groupname=self._groupname)
        nrecords = data.nrecords()
        self.nLoadedRecords = nrecords

        dataMesh = datadict_to_meshgrid(data)
        for avg in self._average_axes:
            if avg in data:
                data = _mesh_mean(dataMesh, avg)

        return dict(dataOut=data)

    def setupUI(self) -> None:
        super().setupUi()


