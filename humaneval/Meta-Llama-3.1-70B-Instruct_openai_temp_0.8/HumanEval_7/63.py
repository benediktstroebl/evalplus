```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to filter by.

    Returns:
        List[str]: Filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage:
if __name__ == "__main__":
    # Test case 1: Empty list
    assert filter_by_substring([], 'a') == []

    # Test case 2: List of strings
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    print("All test cases pass.")
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that include the given substring. The function uses a list comprehension to filter the input list.

The script also includes example usage in the form of test cases, which demonstrate the function's behavior. The `assert` statements check that the function returns the expected output for each test case. If all test cases pass, the script prints a success message.