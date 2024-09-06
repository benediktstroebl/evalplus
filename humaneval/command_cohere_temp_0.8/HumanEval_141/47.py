```python
def file_name_check(file_name):
    checker = filename_checker()
    return "Yes" if checker.is_valid() else "No"

class filename_checker:
    def __init__(self):
        self.name = None
        self.error = None

    def is_valid(self):
        return not self.error

def validate_name(name):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if not name:
        return False, "name is empty"
    if not name.isalpha():
        return False, "should start with a letter"
    if len(name) > 3 and len(name) < 10:
        return False, "should have less than 3 and more than 9 characters"
    if '.' not in name:
        return False, "should contain exactly one dot"
    dot_position = name.find('.')
    pre, post = name[:dot_position], name[dot_position+1:]
    if not set(post).issubset(['txt', 'exe', 'dll']):
        return False, "post dot should be 'txt', 'exe' or 'dll'"
    if not set(pre).issubset(letters):
        return False, "should contain only letters"
    return True, None

def filename_checker():
    name, error = validate_name(self.name)
    self.error = error
    return name is not False
```

The code defines a `filename_checker` class that validates a file name. The `file_name_check` function takes a file name as input and creates a checker instance to validate the file name. 

The `validate_name` function does the actual validation and returns a boolean value and an error message. The `filename_checker` class's `is_valid` method uses this validation function and stores the result for later reference.

The `filename_checker` class is then created, and its `is_valid` method checks the validation result. The previous validation sets an error that can be accessed if the validation returns false. The 'file_name_check' function returns 'Yes' if the file name is valid, and 'No' if it is not.