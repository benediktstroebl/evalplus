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
    """

    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Initialize count to 0
    count = 0

    # Initialize start index to 0
    start = 0

    # Loop until start index is greater than or equal to the length of the string
    while start < len(string):
        # Find the index of the substring in the string, starting from the current start index
        pos = string.find(substring, start)

        # If the substring is not found, break the loop
        if pos == -1:
            break

        # Increment the count
        count += 1

        # Move the start index to the position right after the found substring
        start = pos + 1

    # Return the count
    return count

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

Alternatively, you can use a more Pythonic way to solve this problem using regular expressions:

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
    """

    # Handle edge case where substring is empty
    if not substring:
        return 0

    # Use re.finditer to find all occurrences of the substring
    matches = re.finditer('(?=' + re.escape(substring) + ')', string)

    # Return the number of matches
    return sum(1 for _ in matches)

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```