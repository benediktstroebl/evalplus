```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string. 
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to be searched.

    Returns:
    int: The number of times the substring can be found in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    # Initialize a counter variable to store the count of the substring
    count = 0
    
    # Check if the substring is not empty to avoid infinite loop
    if substring:
        
        # Iterate over the string with a sliding window of size equal to the length of the substring
        for i in range(len(string) - len(substring) + 1):
            
            # Check if the substring matches the current window
            if string[i:i+len(substring)] == substring:
                
                # If it matches, increment the counter
                count += 1
                
    # Return the count of the substring
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```