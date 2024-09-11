```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    count = 0
    i = 0

    # Continue searching for the substring in the string until it's no longer found
    while i < len(string):
        i = string.find(substring, i)

        # If the substring was found, increment the count and move the search position to the character after the found substring
        if i!= -1:
            count += 1
            i += 1
        # If the substring was not found, break out of the loop
        else:
            break

    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script uses a while loop and the `find` method to efficiently search for the substring in the original string. It keeps track of the position where the search should continue (`i`) and increments the count whenever the substring is found. The loop breaks when the substring is no longer found in the string.