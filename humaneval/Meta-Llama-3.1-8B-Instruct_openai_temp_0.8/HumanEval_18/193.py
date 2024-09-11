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
    if not substring:  # edge case: if substring is empty
        return 0
    
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)  # find the next occurrence of the substring
        if index == -1:  # if the substring is not found, break the loop
            break
        count += 1
        index += 1  # move to the next character to avoid finding the same occurrence again
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines the `how_many_times` function which takes a string and a substring as input, and returns the number of times the substring can be found in the string, counting overlapping cases. The script also includes test cases to verify the function's behavior.