```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to search for.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]

# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This script uses a list comprehension to filter the input list of strings. It iterates over each string in the input list and includes it in the output list if the substring is found in the string. The test cases at the end demonstrate its usage.