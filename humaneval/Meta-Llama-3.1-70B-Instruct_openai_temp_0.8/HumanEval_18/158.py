```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:  # Handle the edge case where the substring is empty
        return 0

    count = 0  # Initialize a counter to store the number of occurrences
    start = 0  # Initialize the start index for searching

    while start < len(string):  # Continue searching until the end of the string is reached
        pos = string.find(substring, start)  # Find the position of the substring
        if pos!= -1:  # If the substring is found
            count += 1  # Increment the counter
            start = pos + 1  # Move the start index to the position after the found substring
        else:
            break  # If the substring is not found, break the loop

    return count  # Return the count of occurrences

# Example usage:
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('', 'a'))  # Output: 0
```

Alternatively, you can also solve this problem using a regular expression:

```python
import re

def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
    string (str): The original string to search in.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring is found in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:  # Handle the edge case where the substring is empty
        return 0

    return len(re.findall('(?=' + re.escape(substring) + ')', string))

# Example usage:
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('', 'a'))  # Output: 0
```