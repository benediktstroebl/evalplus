```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the length of the longest string in the list.
    Parameters: List[str]
    Returns: Optional[str]
    """
    longest_len = 0
    max_str = ""
    for string in strings:
        if len(string) > longest_len:
            longest_len = len(string)
            max_str = string
    return max_str if max_str else None
# Example usage
strings = ["a", "b", "c"]
result = longest(strings)
print("The longest string is:", result)
``` 
This function utilizes a loop to iterate through the list of strings, comparing their lengths and storing the longest one in the `max_str` variable. It then returns the'll return `max_str` if it's not `None`, or else return `None`. 

This function is self-contained and efficiently solves the problem of finding the longest string in a given list of strings.