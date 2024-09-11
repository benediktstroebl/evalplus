### Solution
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    index = 0
    
    # Loop through the string until the substring can no longer be found
    while True:
        index = string.find(substring, index)
        
        # If the substring is not found, break the loop
        if index == -1:
            break
        
        # Increment the count and move the index to the next occurrence
        count += 1
        index += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

### Explanation

This script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It uses a while loop to find all occurrences of the `substring` in the `string`. The `find` method returns the index of the first occurrence of the `substring`, or -1 if it's not found. The loop increments the count for each occurrence and moves the index to the next occurrence. The loop breaks when the `substring` can no longer be found in the `string`. The function returns the count of occurrences.