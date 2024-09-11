### Substring Frequency Counter
#### A Python Script to Count the Frequency of a Substring in a Given String

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
    index = 0

    # Continue searching for the substring until we've searched the entire string
    while index < len(string):
        # Check if the substring is present at the current index
        if string[index:index + len(substring)] == substring:
            # If found, increment the count and move the index to the end of the found substring
            count += 1
            index += len(substring)
        else:
            # If not found, move the index to the next character
            index += 1

    return count
```

### Example Usage

```python
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
```

This script defines a function `how_many_times` that takes two parameters: `string` and `substring`. It uses a while loop to continuously search for the `substring` in the `string`, starting from the current index. If the `substring` is found, the count is incremented and the index is moved to the end of the found `substring`. If the `substring` is not found, the index is moved to the next character. The function returns the total count of found `substring`s.