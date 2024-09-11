```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): The substring to search for in the input strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to filter the input list
    # The 'if substring in string' condition ensures only strings containing the substring are included
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    print("All test cases pass.")
```

This script defines a function `filter_by_substring` that filters a list of strings based on whether each string contains a given substring. It uses list comprehension for a concise and efficient solution. The script also includes test cases to verify its correctness.