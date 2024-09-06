```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings (List[str]): list of strings
    Returns:
    str: longest string in the list
    """
    if not strings:
        return None
    return max(strings, key=len)

# Testing the function
strings = ["a", "bb", "ccc"]
longest_result = longest(strings)
print("Longest string:", longest_result)  # Output: "ccc"
``` 
This function, named "longest", takes a list of strings as input and returns the longest string in the list. It utilizes the max function with the `key=len` argument, which ensures that the function returns the string with the maximum length.

It also performs input validation to handle the case when the input list is empty. The test code ensures that the function behaves as expected and returns the correct result for the provided inputs.