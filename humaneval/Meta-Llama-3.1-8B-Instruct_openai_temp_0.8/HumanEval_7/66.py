```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
    strings (List[str]): Input list of strings
    substring (str): Given substring to filter by
    
    Returns:
    List[str]: Filtered list of strings containing the given substring
    
    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    
    # Use list comprehension to filter the list
    # 'if substring in string' checks if the substring is present in each string
    return [string for string in strings if substring in string]


# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Should print []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Should print ['abc', 'bacd', 'array']
```

This script uses list comprehension to efficiently filter the input list of strings. It iterates over each string in the input list and checks if the given substring is present in the string. If the substring is found, the string is included in the filtered list.