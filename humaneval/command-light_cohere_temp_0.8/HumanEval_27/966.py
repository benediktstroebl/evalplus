```python
def flip_case(string):
    return ''.join_case(string.not_case()
   _str(string))

# Test cases
assert flip_case('hello') == 'olleH'
assert flip_case('HEllO') == 'hELLo'
assert flip_case('ABCDEF') == 'cdEFAB'
assert flip_case('@#$%^&*()') == '@#$%^&*'
``` 
This function flip_case takes a string as input and returns a new string with the characters converted to the opposite case.