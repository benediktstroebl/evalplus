### Find Substring Repeats in String
#### Python Solution

```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the original string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    last_position = 0
    while True:
        # Find the position of the substring in the string, starting from the last position
        position = string.find(substring, last_position)
        
        # If the substring is not found, break the loop
        if position == -1:
            break
        
        # Increment the count and update the last position
        count += 1
        last_position = position + 1
    
    return count
```

This script defines a function `how_many_times` that takes a string and a substring as arguments and returns the number of times the substring appears in the string, counting overlapping cases. The function uses a while loop to find the position of the substring in the string, starting from the last position where it was found. If the substring is not found, the loop breaks and the function returns the count.