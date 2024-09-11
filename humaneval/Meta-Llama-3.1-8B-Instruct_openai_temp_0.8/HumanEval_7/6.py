```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to be searched in each string.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

In this script, the function `filter_by_substring` uses list comprehension to create a new list that includes only the strings from the input list that contain the given substring. The test cases are included at the end of the script to verify the function's behavior.