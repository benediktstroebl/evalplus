```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['apple', 'banana', 'orange'], 'an'))  # ['banana', 'orange']
```

This Python script defines a function called `filter_by_substring` that filters a list of strings based on a given substring. It uses a list comprehension to create a new list that only includes the strings from the input list that contain the specified substring. The script also includes some example usage at the end to demonstrate how the function works.