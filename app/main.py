import os


class CleanUpFile:
    def __init__(self, filename:str) -> None:
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self,
                 exc_type,
                 exc_val,
                 exc_tb
                 ) -> bool:
        try:
            os.path.exists(self.filename) and os.remove(self.filename)
        except Exception as e:
            print(f"Error removing file {self.filename} : {e}")
            return False
        return True
