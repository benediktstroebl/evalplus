```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    # Initialize a counter to store the number of occurrences
    count = 0
    
    # Check if the substring is not empty
    if substring:
        # Iterate over the original string
        for i in range(len(string)):
            # Check if the substring matches the current position in the string
            if string[i:i + len(substring)] == substring:
                # If it matches, increment the counter
                count += 1
                
    # Return the total count of occurrences
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It initializes a counter to store the number of occurrences of the substring in the original string. It then iterates over the original string, checking for matches of the substring at each position. If a match is found, the counter is incremented. Finally, the total count of occurrences is returned.