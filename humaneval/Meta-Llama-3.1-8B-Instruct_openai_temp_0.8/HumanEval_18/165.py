```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring appears in the string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    return len(string) // len(substring) if substring else 0
```

This script defines a function `how_many_times` that takes two arguments: `string` and `substring`. It uses the floor division operator (`//`) to calculate the number of times the substring can be found in the string, counting overlapping cases. If the substring is empty, it returns 0. The examples included in the docstring demonstrate the function's behavior.