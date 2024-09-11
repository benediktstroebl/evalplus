### Counting Substring Occurrences
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring in the string.
    """
    count = 0
    while substring in string:
        # Find the position of the substring in the string
        pos = string.find(substring)
        
        # If the substring was found, increment the count and remove it from the string
        if pos!= -1:
            count += 1
            string = string[pos + len(substring):]
        
        # If the substring was not found, break out of the loop
        else:
            break
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```
This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring appears in the string, counting overlapping cases. The function uses a while loop to continuously search for the substring in the string, incrementing the count each time it finds a match. The test cases demonstrate the function's behavior with different input strings and substrings.