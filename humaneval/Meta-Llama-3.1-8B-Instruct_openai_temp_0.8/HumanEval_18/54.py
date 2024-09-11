```python
def how_many Times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    count = 0
    start = 0
    
    # Loop through the string, looking for the substring
    while True:
        index = string.find(substring, start)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count and move the start position to the right
        count += 1
        start = index + 1
    
    # Return the count
    return count


# Test cases
print(how_many Times('', 'a'))  # 0
print(how_many Times('aaa', 'a'))  # 3
print(how_many Times('aaaa', 'aa'))  # 3
```

This script uses a simple loop to find all occurrences of the substring in the original string, incrementing a counter each time the substring is found. The `find` method is used to locate the next occurrence of the substring, and the `start` variable is used to keep track of the position where the next search should start. The loop continues until no more occurrences of the substring are found.