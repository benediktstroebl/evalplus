```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to filter by.
    
    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on the presence of a given substring. It uses a list comprehension to achieve this, making it concise and readable. The function is then tested with two test cases to demonstrate its correctness.