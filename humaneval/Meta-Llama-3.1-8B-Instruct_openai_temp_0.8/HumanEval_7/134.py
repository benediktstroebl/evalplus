### Filtering Strings by Substring
#### Using Python

Here's a Python script that implements the `filter_by_substring` function:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to search for

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    return [s for s in strings if substring in s]

# Example usage:
if __name__ == "__main__":
    # Test case 1: Empty list
    assert filter_by_substring([], 'a') == [], f"Expected [] but got {filter_by_substring([], 'a')}"

    # Test case 2: Non-empty list
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array'], \
        f"Expected ['abc', 'bacd', 'array'] but got {filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')}"
```

This script defines the `filter_by_substring` function using a list comprehension to filter the input list of strings based on whether they contain the given substring. It then includes example usage and test cases to demonstrate the function's correctness.