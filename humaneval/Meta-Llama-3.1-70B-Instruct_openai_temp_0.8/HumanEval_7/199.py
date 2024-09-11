Here's a simple Python script that defines the `filter_by_substring` function and includes some example use cases:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring that filtered strings should contain.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]

# Example use cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello world', 'foo bar', 'baz'], 'world'))  # Expected output: ['hello world']
print(filter_by_substring(['python', 'java', 'c++'], 'py'))  # Expected output: ['python']
```

This script uses list comprehension to create a new list containing only the strings from the input list that include the specified substring. The `in` operator checks for substring presence in each string.