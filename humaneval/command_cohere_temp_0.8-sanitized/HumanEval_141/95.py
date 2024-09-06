import pytest
def file_name_check(file_name):
    checker = lambda s: len(s) <= 1 and s[0] in '.abcdeikljopqstvwxyzACDEFGHIKLMNOQRSTUVWXYZ'
    filename, extension = file_name.split('.')
    if len(filename) == 0 or not all(checker(c) for c in filename) or len(extension) != 3 or not all(c in 'txtexedll' for c in extension):
        return "No"
    return "Yes"