Here is a Python script with a self-contained function that solves the problem of concatenating a list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # create an empty string to concatenate
    result = ''
    
    # iterate through list and concatenate strings
    for string in strings:
        result += string
    
    return result
#tests
def test_concatenate():
    # list with empty string
    strings = []
    strings.append('a')
    
    # test case 1: empty list
    result = concatenate(strings)
    assert result == ''
    
    # test case 2: list with one string
    strings.append('a')
   
    result = concatenate(strings)
    assert result == 'a'
    
    # test case 3: list with two strings
    strings.append('b')
    string1 = 'ab'
    strings.append('c')
    string2 = 'c'
    result = concatenate(strings)
    assert result == 'abc'
    
    return 
``` 
This script provides a function `concatenate` that takes a list of strings as input and concatenates them into a single string. It also includes tests that check the expected output of the `concatenate` function for different inputs.