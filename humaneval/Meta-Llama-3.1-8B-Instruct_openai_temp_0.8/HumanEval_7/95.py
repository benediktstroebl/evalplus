```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: A new list containing only the strings that contain the substring
    """
    # Use list comprehension to create a new list containing only strings that contain the substring
    return [s for s in strings if substring in s]

# Example usage:
if __name__ == "__main__":
    # Test cases
    print(filter_by_substring([], 'a'))  # []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # ['hello', 'python']
    print(filter_by_substring(['123', '456', '789'], '0'))  # []
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses list comprehension to create a new list containing only the strings that contain the substring. The function is then tested with example usage in the `if __name__ == "__main__":` block.