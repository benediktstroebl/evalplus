Here is a Python script that contains a self-contained function that filters an input list of strings for a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings for the substring
    :param strings: List of strings
    :param substring: Substring to filter
    :return: List of strings containing the substring
    """
    return [s for s in strings if substring in s]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hyper"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
``` 

This script defines a function `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). It then returns a new list containing only the strings from the input list that contain the given substring. 

The test cases demonstrate how the function works by filtering the strings list for a specific substring.