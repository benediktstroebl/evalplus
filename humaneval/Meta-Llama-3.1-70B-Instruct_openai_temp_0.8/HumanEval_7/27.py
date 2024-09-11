```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to look for in the list of strings.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

if __name__ == "__main__":
    print("All test cases pass")
```
In this script, we use a list comprehension to generate a new list that only includes the strings from the input list that contain the given substring. The `in` operator is used to check if the substring is present in each string. The test cases are run using the `assert` statement, and if all test cases pass, a success message is printed.