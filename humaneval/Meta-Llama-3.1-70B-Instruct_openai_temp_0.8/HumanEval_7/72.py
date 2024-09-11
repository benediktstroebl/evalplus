```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.
    
    Args:
        strings (List[str]): A list of strings.
        substring (str): The substring to filter by.
    
    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
print("All test cases passed.")
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings. It includes a docstring with a description, parameters, and return value. The test cases are also included to verify the correctness of the function. If all test cases pass, it prints "All test cases passed."