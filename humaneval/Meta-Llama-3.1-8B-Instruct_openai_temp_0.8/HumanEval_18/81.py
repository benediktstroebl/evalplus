```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring can be found in the original string.
    """
    if not substring:  # edge case: if the substring is empty
        return 0
    
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1  # move the start pointer to the right of the found substring
        else:
            break
    
    return count

# Example use cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that uses a while loop to repeatedly search for the given substring in the original string, starting from the current position. When the substring is found, the function increments the count and moves the start pointer to the right of the found substring. If the substring is not found, the function breaks out of the loop. The function then returns the count of times the substring was found.