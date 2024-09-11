```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to filter by.

    Returns:
        List[str]: Filtered list of strings.
    """
    return [string for string in strings if substring in string]


# Example use cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that uses list comprehension to filter the input list `strings` based on the presence of the given `substring`. It checks if the `substring` is present in each string using the `in` operator, and includes only those strings in the output list. The function is accompanied by a docstring that describes its purpose, parameters, and return value. Additionally, example use cases are provided to demonstrate the function's behavior.