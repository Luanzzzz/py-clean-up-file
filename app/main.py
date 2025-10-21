import os
from typing import Optional, Type
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename:str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> bool:
        try:
            os.path.exists(self.filename) and os.remove(self.filename)
        except Exception as e:
            print(f"Error removing file {self.filename} : {e}")
            return False
        return True
