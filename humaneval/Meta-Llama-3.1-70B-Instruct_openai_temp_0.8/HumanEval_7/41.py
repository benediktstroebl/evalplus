```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings. The list comprehension iterates over each string in the input list and checks if the substring is present in the string using the `in` operator. If the substring is found, the string is included in the output list.

The script also includes two test cases to verify the correctness of the function. The first test case checks that an empty list is returned when the input list is empty. The second test case checks that the function correctly filters the input list based on the given substring.