```python
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
```
This approach splits the file name into parts using the period as the delimiter. It then checks the length, starting letter, and validity of the second part as per the problem statement requirements. The method `is_latin_prefix` checks for the first letter validity and whether the rest of the letters are alphanumeric. The static method (`@staticmethod`) is a decorator that allows you to make a method behave as a function. 

The following is a test drive function you may use to check the `file_name_check` function.
```python
def test_file_name_check():
    # Valid Names
    assert file_name_check("example.txt") == "Yes"
    assert file_name_check("a_sample.exe") == "Yes"
    assert file_name_check("brazil.dll") == "Yes"

    # Invalid Names
    assert file_name_check("1example.dll") == "No"
    assert file_name_check("exe") == "No"
    assert file_name_check("____.txt") == "No"
    assert file_name_check("a.txt") == "No"
    assert file_name_check("abc1.txt") == "No"

test_file_name_check()
```
This will ensure that the script performs as expected. 

This solution provides a concise way to handle the file name validation problem and can be easily adapted to handle other file name rules if needed.