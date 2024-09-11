```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to filter by.

    Returns:
        List[str]: The filtered list of strings.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  #[]
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  #['abc', 'bacd', 'array']
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'))  #[]
```

In this script, a list comprehension is used to create a new list that includes only the strings from the input list that contain the given substring. This script also includes a few test cases to demonstrate the function's behavior.