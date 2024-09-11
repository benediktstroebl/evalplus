### Filter List of Strings by Substring
#### Description
This Python script defines a function `filter_by_substring` that filters a list of strings based on the presence of a given substring.

#### Code
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for in each string.

    Returns:
        List[str]: The filtered list of strings containing the substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    filtered_strings = filter_by_substring(strings, substring)
    print(f"Strings containing '{substring}': {filtered_strings}")
```
#### Explanation
The `filter_by_substring` function uses a list comprehension to create a new list containing only the strings that include the specified substring. This is achieved by iterating over the input list and using the `in` operator to check if each string contains the substring. If it does, the string is included in the new list.