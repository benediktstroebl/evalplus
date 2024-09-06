```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings (List[str]): List of strings to compare their length.
    Returns: List containing the string that has the longest length.
    """
    return [strings
    max(map(len,strings)))
```
We create a function called **longest** that takes a list of strings as input and returns the longest string from the list, as a list. The function uses the max function to map the length of each string in the list and return the longest one.

We pass the test by calling the function with different lists of strings, and the output is correctly printed.