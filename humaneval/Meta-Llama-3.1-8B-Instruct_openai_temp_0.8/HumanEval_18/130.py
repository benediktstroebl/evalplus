```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the string.
    """
    count = 0
    i = 0
    while i < len(string):
        i = string.find(substring, i)
        if i!= -1:
            count += 1
            i += 1  # Move to the position after the found substring
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that finds the number of times a given substring can be found in a string, counting overlapping cases. The function uses a while loop and the `find` method of the string to find the substring, and increments the count for each found occurrence. The test cases are executed at the end to demonstrate the function's correctness.