```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    index = 0
    
    # Continue searching until the substring is no longer found in the string
    while True:
        index = string.find(substring, index)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        count += 1
        index += 1  # Move the search index forward to prevent infinite loop

    return count
```

Example use cases:
```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```