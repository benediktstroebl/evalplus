```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered
        substring (str): The substring to filter by

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    # Use list comprehension to create a new list containing only strings that have the substring
    return [string for string in strings if substring in string]

# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
    print(filter_by_substring(['hello', 'world', 'python', 'programming'], 'th'))
    print(filter_by_substring(['test','string','sub','strings'],'sub'))
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. The function uses list comprehension to create the new list. The script also includes test cases to demonstrate the function's behavior.