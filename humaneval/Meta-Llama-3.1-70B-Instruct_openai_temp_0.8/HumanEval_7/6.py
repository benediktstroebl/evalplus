**Solution**
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```
**Explanation**

This script uses a list comprehension to create a new list that only includes strings from the input list that contain the given substring. The `in` operator is used to check if the substring is present in each string.

**How it works**

1. The function `filter_by_substring` takes two parameters: `strings` (a list of strings) and `substring` (a string to filter by).
2. The list comprehension iterates over each string `s` in the input list `strings`.
3. For each string, it checks if the `substring` is present using the `in` operator.
4. If the substring is found, the string is included in the new list.
5. The resulting list is returned by the function.

This solution is concise, efficient, and meets the requirements specified in the docstring.