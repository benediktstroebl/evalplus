```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to search for in each string.

    Returns:
        List[str]: Filtered list of strings containing the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    # Initialize an empty list to store filtered strings
    filtered_strings = []

    # Iterate over each string in the input list
    for string in strings:
        # Check if the substring is present in the current string
        if substring in string:
            # If the substring is found, append the string to the filtered list
            filtered_strings.append(string)

    # Return the filtered list of strings
    return filtered_strings

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```