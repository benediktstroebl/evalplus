```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered
        substring (str): The substring to search for in the input strings

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to filter the input list and returns a new list containing only the strings that contain the given substring. The test cases are included to verify the correctness of the function.