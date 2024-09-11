```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): The substring to search for.

    Returns:
        List[str]: A filtered list of strings containing the given substring.

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
    result = filter_by_substring(strings, substring)
    print(result)  # Output: ['abc', 'bacd', 'array']
```

In this script, the function `filter_by_substring` uses a list comprehension to filter the input list of strings. It checks each string in the list to see if it contains the given substring and includes it in the output list if it does. The script then includes an example usage of the function, demonstrating its effectiveness with the provided test cases.