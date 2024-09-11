```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to find.

    Returns:
        int: The number of times the substring can be found.
    """
    if not substring:  # if the substring is empty, return 0
        return 0

    count = 0  # initialize the count
    start = 0  # initialize the start index

    while start < len(string):  # loop through the string
        pos = string.find(substring, start)  # find the substring
        if pos!= -1:  # if found
            count += 1  # increment the count
            start = pos + 1  # move the start index to the next position
        else:
            break  # if not found, stop the loop

    return count


# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```