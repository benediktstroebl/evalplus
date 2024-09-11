```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.
    """
    count = 0
    i = 0
    while i < len(string):
        # Find the index of the substring in the string starting from the current index
        index = string.find(substring, i)
        # If the substring is found, increment the count and move the index forward
        if index!= -1:
            count += 1
            i = index + 1
        # If the substring is not found, break out of the loop
        else:
            break
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses the `find` method of Python strings to search for the substring in the original string. It starts searching from the current index `i` and increments `i` each time the substring is found. If the substring is not found, the loop breaks and the function returns the count.