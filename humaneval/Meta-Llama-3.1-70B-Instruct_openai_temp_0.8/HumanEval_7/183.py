```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to search for.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]

# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
print("All test cases pass.")
```

This Python script defines a function `filter_by_substring` that filters an input list of strings and returns only the strings that contain a given substring. The function uses a list comprehension to create the filtered list.

The script includes two test cases to verify the function's correctness. The `assert` statements check if the function's output matches the expected output. If the function passes both test cases, it prints "All test cases pass."