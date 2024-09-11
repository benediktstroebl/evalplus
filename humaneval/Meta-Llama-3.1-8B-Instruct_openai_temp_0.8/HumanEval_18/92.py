### Find the number of occurrences of a substring in a string
#### Python Solution

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of occurrences of the substring in the string.

    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    index = 0
    while index < len(string):
        index = string.find(substring, index)
        if index!= -1:
            count += 1
            index += 1
        else:
            break
    return count
```

This function uses the `find()` method of the string class, which returns the index of the first occurrence of the substring. If the substring is not found, it returns -1. The loop continues until the substring is not found in the string. The index is incremented by the length of the substring in each iteration to ignore overlapping cases.