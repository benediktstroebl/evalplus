```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): List of strings to be filtered
        substring (str): The substring to search for in each string
        
    Returns:
        List[str]: List of strings that contain the given substring
    """
    # Use list comprehension to create a new list containing only strings that include the substring
    return [s for s in strings if substring in s]


# Test cases
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Expected output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on whether each string contains a specified substring. It uses a list comprehension to achieve this in a concise and efficient manner. The script also includes test cases to demonstrate the function's behavior.