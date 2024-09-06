```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)

# Test the function with different inputs
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
strings = [' '.join(i) for i in 'abc' ]
print(concatenate(strings))  # Output: 'abc'
``` 
This function, `concatenate`, takes a list of strings as input and returns the concatenated string. It uses the `join string `join()` to concatenate the strings.

This is a self-contained function, meaning it can be used without depending on any other functions or modules. It passes all the specific inputs and outputs, and the test cases show that the function works correctly for different combinations of strings.