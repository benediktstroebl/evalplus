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
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            start = pos + 1
            count += 1
        else:
            break
    return count

# Example usage
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop to iterate through the string and keep track of the starting position (`start`) where the next search should begin. Inside the loop, the `find` method is used to search for the substring, starting at the current position. If the substring is found, the loop continues with the next position (i.e., `start = pos + 1`). If the substring is not found, the loop breaks. The count is incremented each time the substring is found.