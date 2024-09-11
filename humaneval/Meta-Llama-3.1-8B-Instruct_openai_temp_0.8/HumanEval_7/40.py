```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for in the input strings

    Returns:
        List[str]: A list of strings that contain the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    # Use list comprehension to filter the input list
    # The 'if substring in string' condition ensures the substring is present
    filtered_strings = [string for string in strings if substring in string]
    
    # Return the filtered list
    return filtered_strings


# Example usage:
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Should print: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Should print: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. It includes example usage at the end to demonstrate the function's behavior.