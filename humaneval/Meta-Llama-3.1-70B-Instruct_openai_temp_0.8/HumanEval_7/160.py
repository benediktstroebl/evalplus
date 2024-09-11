```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
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

    strings = []
    substring = 'a'
    result = filter_by_substring(strings, substring)
    print(result)  # Output: []
```
This script defines the `filter_by_substring` function as requested. The function uses a list comprehension to create a new list that includes only the strings from the input list that contain the given substring. 

The script also includes example usage in the `if __name__ == "__main__":` block. This block is executed when the script is run directly, but not when it is imported as a module in another script. The examples demonstrate the function's behavior with both a non-empty list of strings and an empty list.