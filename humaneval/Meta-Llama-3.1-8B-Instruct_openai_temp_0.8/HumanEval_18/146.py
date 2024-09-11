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
    if not substring:  # If the substring is empty, return 0
        return 0

    start = 0
    while True:
        start = string.find(substring, start)  # Find the substring in the string
        if start!= -1:  # If the substring is found
            count += 1  # Increment the count
            start += 1  # Move the start position forward
        else:
            break

    return count


# Example usage
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines a function `how_many_times` that takes a string and a substring as input and returns the number of times the substring can be found in the string, counting overlapping cases. It uses a while loop to iteratively find the substring in the string, incrementing the count each time it's found. The loop breaks when the substring is no longer found. The script includes example usage at the end.