```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to filter by.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [s for s in strings if substring in s]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

if __name__ == "__main__":
    print("All test cases pass.")
```

This script defines the `filter_by_substring` function that uses a list comprehension to filter the input list of strings. The function includes a docstring that describes its behavior, arguments, and return value.

The script also includes two test cases to verify the correctness of the function. If all test cases pass, it prints a success message.

You can run this script directly to test the function.