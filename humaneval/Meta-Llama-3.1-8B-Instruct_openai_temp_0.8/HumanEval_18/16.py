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
    if not substring:  # edge case: empty substring
        return 0
    
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(substring):  # check if string starts with substring
            count += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes in a string and a substring, and returns the number of times the substring can be found in the string. The function uses a for loop to iterate over the string, and checks if the substring is present at each position. If the substring is found, the function increments the count. The function returns the count at the end. The test cases are included to demonstrate the function's usage.