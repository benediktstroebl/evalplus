```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string from a list of strings.
    Args:
    strings (List[str]): list of strings.
    Returns the longest string in the list of strings
    Returns:
    List of the longest string in each string list
    """
    result = [string.join('').join(strings) for string in strings if len(string) == max(map(len, strings))]
    return result
``` 
You can use this to solve the problem of finding the longest string in an array of markdown code blocks.