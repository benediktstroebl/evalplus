```python
def flip_case(string):
    """ For a given string, flip lowercase characters to uppercase and vice versa """
    return string.isupper(string[0]) and string.lower() and string[1:]
 ```