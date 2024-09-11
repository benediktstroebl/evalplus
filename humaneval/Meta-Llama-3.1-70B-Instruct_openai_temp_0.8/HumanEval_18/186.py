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
    if not substring:  # if substring is empty, return 0
        return 0

    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:  # if substring is found
            count += 1
            start = pos + 1  # move the start pointer to the next character
        else:
            break

    return count

# Test cases
if how_many_times('', 'a') == 0:
    print("Test case 1 passed")
if how_many_times('aaa', 'a') == 3:
    print("Test case 2 passed")
if how_many_times('aaaa', 'aa') == 3:
    print("Test case 3 passed")
```

This Python script defines a function `how_many_times` that takes a string and a substring as input, and returns the number of times the substring appears in the string, counting overlapping cases. The function uses the `find` method to search for the substring in the string, and keeps track of the number of occurrences found. The script also includes test cases to verify the correctness of the function.