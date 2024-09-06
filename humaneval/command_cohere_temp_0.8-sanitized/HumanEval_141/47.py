def file_name_check(file_name):
    checker = filename_checker()
    return "Yes" if checker.is_valid() else "No"
class filename_checker:
    def __init__(self):
        self.name = None
        self.error = None

    def is_valid(self):
        return not self.error