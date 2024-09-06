Here is a Python script that includes the self-contained function **`filter_by_substring`** which is designed to solve the problem you have described: 
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    :param strings: List of strings
    :param substring: Substring to filter
    :return: List of strings that contain the given substring
    """
    return [string for string in strings if string.contains(substring)]
```

This function uses a list comprehension to iterate over each string in the input list. It then uses the string.contains() method to check if each string contains the given substring.