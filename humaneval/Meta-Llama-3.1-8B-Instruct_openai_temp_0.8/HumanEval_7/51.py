```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to search for in the input list.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    # Use list comprehension to create a new list containing only the strings that have the substring
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    assert filter_by_substring([], 'a') == []
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    print("All test cases passed!")
```
This script defines the `filter_by_substring` function, which takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. The function uses list comprehension to achieve this. The script also includes test cases to verify the function's correctness.