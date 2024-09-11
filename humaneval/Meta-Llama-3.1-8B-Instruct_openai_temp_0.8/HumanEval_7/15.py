```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to filter
        substring (str): A substring to search in each string

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    # Use list comprehension to filter the list of strings
    # The 'if substring in string' condition filters out strings that don't contain the substring
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    print("All test cases passed!")
```

This script defines the `filter_by_substring` function as requested and includes two test cases to verify its correctness. The function uses list comprehension to filter the input list of strings based on whether they contain the given substring. The `if __name__ == "__main__"` block runs the test cases when the script is executed directly.