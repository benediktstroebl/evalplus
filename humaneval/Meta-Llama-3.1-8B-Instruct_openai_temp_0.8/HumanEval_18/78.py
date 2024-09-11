```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    if len(substring) == 0:  # edge case: empty substring
        return 0
    
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)  # find the next occurrence
        if index!= -1:  # if the substring was found
            count += 1  # increment the count
            index += 1  # move the index past the found substring
        else:
            break  # if the substring was not found, exit the loop
    
    return count

# Test cases
print(how_many_times('', 'a'))  # expected output: 0
print(how_many_times('aaa', 'a'))  # expected output: 3
print(how_many_times('aaaa', 'aa'))  # expected output: 3
```

This script defines a function `how_many_times` that takes a string and a substring as input. It uses a while loop to find the first occurrence of the substring in the string, and then continues to find subsequent occurrences, counting each one. If the substring is not found, the loop exits. The function returns the total count of occurrences. The script includes test cases to demonstrate the function's behavior.