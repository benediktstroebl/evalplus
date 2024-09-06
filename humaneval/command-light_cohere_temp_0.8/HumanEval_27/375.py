```python
def flip_case(string):
    return ''.join_\26(string)
    
if __name__ == "__main__":
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'oRDlU'
    assert flip_case('hello world') == 'Hllo Wrdl'
    assert flip_case('FOO Bar') == 'BAo ROOF'
    assert flip_case('hello@example.com') == 'HEllox e mxnp'
 ``` 
This script defines a function `flip_case` which takes a string as input and returns a new string with the characters reversed. The `__name__ == "__main__"` check ensures that the function is only executed when run as the script, preventing accidental imports.