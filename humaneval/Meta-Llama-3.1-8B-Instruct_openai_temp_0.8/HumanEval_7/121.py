```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    - strings (List[str]): Input list of strings
    - substring (str): The substring to be searched in the input strings

    Returns:
    - List[str]: Filtered list of strings containing the given substring
    """
    return [string for string in strings if substring in string]

# Example usage
if __name__ == "__main__":
    # Test case 1: Empty list
    print(filter_by_substring([], 'a'))
    
    # Test case 2: List with strings containing the substring
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
    
    # Test case 3: List with strings not containing the substring
    print(filter_by_substring(['cde', 'xyz', 'ghi'], 'a'))
```

The provided Python script uses list comprehension to create a new list that includes only the strings from the input list that contain the given substring. The code includes example usage and test cases to demonstrate its functionality. The script adheres to the provided docstring and type hints.