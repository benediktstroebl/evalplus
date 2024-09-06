```python
def longest(strings: List[str]) -> Optional[str]:
    # Check for empty list
    if not strings:
        return None
    
    # Sort strings
    strings.sort()
    
    # Check length of strings
    max_length = max(len(str) for str in strings)
    
    # Find the longest string
    longest_string = strings[max_length - 1]
    
    return longest_string
```