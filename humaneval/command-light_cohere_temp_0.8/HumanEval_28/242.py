```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test cases
strings = ["a", "bc", "d"]
print(concatenate(strings))  # Output: abc
strings = []
print(concatenate(strings))  # Output: 

strings = ["passive", "see you"]
print(concatenate(strings))  # Output: see you

```
This Python code defines a function **concatenate** that takes a list of strings as an argument and concatenates them into a single string. The code also provides a series of test cases to ensure the correctness of the **concatenate** function.