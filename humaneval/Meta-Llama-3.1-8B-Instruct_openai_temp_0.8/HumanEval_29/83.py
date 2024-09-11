```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bcd', 'cde', 'array']
    prefix = 'a'
    filtered_strings = filter_by_prefix(strings, prefix)
    
    print(f"Original List: {strings}")
    print(f"Filtered List (prefix '{prefix}'): {filtered_strings}")
```

In this script, we use a list comprehension to create a new list that includes only the strings from the input list that start with the given prefix. The `startswith` method is used to check if a string begins with the specified prefix.