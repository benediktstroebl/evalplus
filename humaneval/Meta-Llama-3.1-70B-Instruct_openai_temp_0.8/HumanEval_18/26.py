```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring appears in the string.
    """
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos!= -1:
            count += 1
            start = pos + 1
        else:
            break
    return count


# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

This script defines a function `how_many_times` that takes two parameters, `string` and `substring`. It then uses a while loop to find all occurrences of the substring in the string, counting overlapping cases. The `find` method is used to get the position of the substring in the string, and the `start` variable is updated to continue searching from the next position.

The test cases are provided using Python's built-in `assert` statement, which checks if the condition given is true. If it's not, an `AssertionError` is raised.