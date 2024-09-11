```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be found.

    Returns:
        int: The number of times the substring is found in the string.
    """
    if not substring:  # If the substring is empty, return 0
        return 0
    
    count = 0  # Initialize a counter variable
    start = 0  # Initialize a start index
    
    while start < len(string):  # Iterate through the string
        pos = string.find(substring, start)  # Find the substring in the string, starting from the current index
        
        if pos!= -1:  # If the substring is found
            count += 1  # Increment the counter
            start = pos + 1  # Move the start index to the character after the found substring
        else:
            break  # If the substring is not found, break the loop
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring is found in the string, counting overlapping cases. The function uses a while loop to iterate through the string, finding the substring and incrementing a counter each time it is found. The start index is moved to the character after the found substring to allow for overlapping cases. If the substring is empty, the function returns 0. The script also includes test cases to demonstrate the function's behavior.