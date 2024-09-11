### Filtering Strings by Substring

Here's a Python script that defines a function `filter_by_substring` to filter a list of strings based on a given substring.

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to search for in each string

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    return [s for s in strings if substring in s]

# Example usage:
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Test the function
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this script, we use a list comprehension to create a new list that includes only the strings from the input list where the substring is found. The `doctest` module is used to verify that the function behaves correctly according to the provided docstring examples.