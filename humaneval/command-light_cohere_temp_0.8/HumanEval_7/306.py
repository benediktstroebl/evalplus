Here is a Python script that includes the function `filter_by_substring`, which is designed to solve the problem you provided:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings
        substring (str): Substring to find

    Returns:
        List[str]: List of strings that contain the substring
    """
    return [string for string in strings if string.contains(substring)]
```

This script defines a function that takes in a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. 

This function uses the string method `contains()` to check if each string in the input list contains the given substring, and the list comprehension `[string for string in strings]` to filter out the strings that do not contain the substring.