def file_name_check(file_name):
    checker = fileNameChecker(file_name)
    return "Yes" if checker.isValid() else "No"
class fileNameChecker:
    def __init__(self, file_name):
        self.file_name = file_name
    def isValid(self):
        digits_count = sum(char.isdigit() for char in self.file_name)
        return (
            self.file_name.count('.') == 1 and
            self.file_name[0].isalpha() and 
            self.file_name[-3:-1].isalpha() and 
            self.file_name[-2:] in ['txt', 'exe', 'dll'] and 
            digits_count <= 3
        )