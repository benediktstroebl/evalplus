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
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1

    return count

# test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

However, the above approach has a time complexity of O(n*m), where n is the length of the string and m is the length of the substring. We can improve this to O(n) using a more efficient algorithm.

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
    if not substring:  # edge case: empty substring
        return 0

    count = 0
    i = 0
    while i < len(string):
        if string[i:i + len(substring)] == substring:
            count += 1
            i += 1  # move forward by one character
        else:
            i += 1

    return count

# test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```

But, a more pythonic and efficient way to solve this is using `str.count()` or a list comprehension with a sliding window approach:

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
    if not substring:  # edge case: empty substring
        return 0

    return sum(1 for i in range(len(string) - len(substring) + 1) if string[i:i + len(substring)] == substring)

# test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
```