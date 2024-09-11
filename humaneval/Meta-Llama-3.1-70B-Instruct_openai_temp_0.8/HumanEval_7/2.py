```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    - strings (List[str]): A list of strings to filter.
    - substring (str): The substring to search for in the strings.

    Returns:
    - List[str]: A list of strings from the input list that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

if __name__ == "__main__":
    print("All test cases passed.")
```
This script defines the `filter_by_substring` function as requested and includes test cases to verify its correctness. If the function passes all test cases, it prints "All test cases passed."