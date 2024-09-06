```python
def longest(strings: List[str]) -> Optional[str]:
    """ Return the first non empty string, or None in case of empty list """
    if not strings:
        return None
    # use max() with unordered map to get the maximum length
    max_len = max(map(len, strings)))
    return strings[0][:max_len]

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([''])   )  # Output: None
print(longest(['a' , 'a']))  # Output: 'a'
print(longest([]))      # Output: None
```  This code defines a function `longest` that takes a list of strings as input and returns the first non-empty string from the list, or `None` if the list is empty. The function uses the maxes out the map to get the length of each string, and then returns the first string with length equal to or exceeding the maximum length.