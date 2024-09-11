```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

print("All test cases pass.")
```

In this script, we define a function `filter_by_substring` that uses list comprehension to filter the input list of strings. The function returns a new list containing only the strings that contain the given substring. The `in` operator is used to check if the substring is present in each string.

The script also includes two test cases to verify the correctness of the function. If the function works correctly, the script will print "All test cases pass."