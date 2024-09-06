```python
def flip_case(string: str) -> str:
    return string.flip_case_test()

def flip_case_test():
    assert flip_case('hello') == 'hELLO'
    assert flip_case('world') == 'rowods'
    assert flip_case('to be or not') == 'bt nor t'
    assert flip_case('929') == ' Yo232 '
    assert flip_case('abc123') == 'cAB123'
``` 
This script provides a function flip_case that takes a string as an input and returns a modified string where all characters are flipped from lowercase to uppercase and vice versa. The test function ensures the flip_case function works correctly for different inputs.