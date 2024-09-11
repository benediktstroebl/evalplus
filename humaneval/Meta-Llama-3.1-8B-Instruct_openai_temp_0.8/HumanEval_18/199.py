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

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not substring:
        return 0  # Handle the case when the substring is empty

    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1  # Move the index to the character after the found substring
        else:
            break

    return count
```

This Python script defines a function `how_many_times` that takes two string parameters: the original string and the substring to search for. It returns the number of times the substring can be found in the original string, counting overlapping cases. The function uses a while loop to continuously search for the substring in the string, starting from the current index. It keeps track of the count and increments it each time the substring is found. If the substring is not found at the current index, it breaks the loop and returns the count.