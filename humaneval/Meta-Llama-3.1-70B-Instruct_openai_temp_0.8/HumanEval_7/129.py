```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring that must be present in the filtered strings.
    
    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to create a new list that only includes strings containing the substring
    return [s for s in strings if substring in s]


# Example usage
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this script, the `filter_by_substring` function takes a list of strings and a substring as input, then uses list comprehension to create a new list that only includes strings that contain the given substring. This is achieved using the condition `substring in s` for each string `s` in the input list. The script also includes example usage in the `if __name__ == "__main__":` block to demonstrate how to call the function with different inputs.