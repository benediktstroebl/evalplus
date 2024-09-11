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
    count = 0
    if not substring:  # edge case: if substring is empty, return 0
        return count

    for i in range(len(string)):
        if string[i:].startswith(substring):  # check if string starts with substring
            count += 1

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring can be found in the string, including overlapping cases. It uses a simple loop to check each position in the string to see if it starts with the substring, and increments a count each time it finds a match. If the substring is empty, it immediately returns 0. Finally, it includes some test cases to demonstrate its usage.