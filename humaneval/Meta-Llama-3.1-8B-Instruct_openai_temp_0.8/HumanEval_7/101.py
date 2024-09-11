```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to search for in the strings
        
    Returns:
        List[str]: Filtered list of strings containing the substring
    """
    return [string for string in strings if substring in string]

# Example usage
if __name__ == "__main__":
    strings = ['abc', 'bacd', 'cde', 'array', 'xyz']
    substring = 'a'
    result = filter_by_substring(strings, substring)
    print(result)  # Output: ['abc', 'bacd', 'array']

# Test cases
try:
    assert filter_by_substring([], 'a') == []
except AssertionError:
    print("Test case 1 failed")

try:
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
except AssertionError:
    print("Test case 2 failed")
```