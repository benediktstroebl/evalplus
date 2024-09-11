```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if not string or not substring:
        return 0
    
    count = 0
    index = 0
    
    while index < len(string):
        index = string.find(substring, index)
        
        if index!= -1:
            count += 1
            index += 1  # Move to the next character after finding the substring
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Expected output: 0
print(how_many_times('aaa', 'a'))  # Expected output: 3
print(how_many_times('aaaa', 'aa'))  # Expected output: 3
```

This script defines a function `how_many_times` that finds the number of times a given substring appears in a string, counting overlapping cases. It uses the `find` method of the string class to find the substring, and then increments the count for each occurrence. If the substring is not found, the function breaks out of the loop. The script also includes test cases to verify the correctness of the function.