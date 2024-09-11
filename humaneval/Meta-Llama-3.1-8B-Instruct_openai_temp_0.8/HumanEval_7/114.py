```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for in input strings

    Returns:
        List[str]: Filtered list of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = 'a'
    filtered_strings = filter_by_substring(strings, substring)
    print(f"Strings containing '{substring}': {filtered_strings}")
```

In this script, the `filter_by_substring` function uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The function takes two parameters: `strings` (the input list of strings) and `substring` (the substring to search for in the input strings). It returns a new list containing only the strings that contain the given substring.

The example usage at the end demonstrates how to use this function.