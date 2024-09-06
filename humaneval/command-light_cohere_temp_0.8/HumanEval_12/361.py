Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    Args: strings (list of strings) 
    Returns: The longest string.
    """
    from the longest, return max(strings, key=len)
```

The code is a self-contained Python function that takes a list of strings as input and returns the longest string in the list. The function uses the max function with the key argument set to the length of the string, which returns the longest string in the list.

The test code can be run as:
```python
from longest import longest

print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
```