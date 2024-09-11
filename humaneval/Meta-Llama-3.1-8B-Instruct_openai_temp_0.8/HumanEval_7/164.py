```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to filter by

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    print("All test cases passed!")
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses a list comprehension to create a new list containing only the strings that contain the substring. The test cases at the end of the script demonstrate the function's behavior.