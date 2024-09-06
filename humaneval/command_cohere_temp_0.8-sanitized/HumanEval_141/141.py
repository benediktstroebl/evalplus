def file_name_check(file_name):
    checker = ValidFileNameChecker()
    return "Yes" if checker.is_valid_name(file_name) else "No"
class ValidFileNameChecker:
    def __init__(self):
        self.valid_file_types = ["txt", "exe", "dll"]
        self.latin_prefix = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def is_valid_name(self, file_name):
        file_name = str(file_name).strip()
        if not file_name:
            return False

        parts = file_name.split(".")
        if len(parts) != 2:
            return False

        prefix = parts[0]
        file_extension = parts[1]

        if not prefix:
            return False
        if not self.is_latin_prefix(prefix):
            return False
        if len(prefix) > 10:
            return False
        if len(file_extension) > 10:
            return False
        if file_extension not in self.valid_file_types:
            return False
        return True

    @staticmethod
    def is_latin_prefix(word):
        return word[0] in ValidFileNameChecker.latin_prefix and word[1:].isalnum()