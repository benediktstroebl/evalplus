Here's the solution:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        str: concatenated string
    """
    return ''.join(strings)
# Example test cases
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
strings = ['aa', 'bb', 'cc']
print(concatenate(strings))  # Output: 'awtcc'
```
This code defines the **concatenate** function, which takes a list of strings as input and returns the concatenated string by invoking the **join()** method. The output of the example test cases demonstrates the usage of the function, showing the expected results.