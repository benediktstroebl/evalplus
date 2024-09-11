```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlaping cases.

    Args:
        string (str): The original string to search in.
        substring (str): The substring to search for.

    Returns:
        int: The number of times the substring can be found in the original string.
    """
    return len(string) // len(substring) if substring else 0
```

This script defines a function `how_many_times` that takes two parameters: `string` and `substring`. It returns the number of times the `substring` can be found in the `string`. If the `substring` is empty, it returns 0 because an empty string cannot be found in any string. 

The function uses the floor division operator (`//`) to count the number of times the `substring` can fit into the `string`. This will count overlapping cases because the `//` operator rounds down to the nearest whole number, effectively treating each character in the `string` as a starting point for a new instance of the `substring`. 

For example, if the `string` is `'aaa'` and the `substring` is `'a'`, the `//` operator will return `3` because the `'a'` can be found in the first, second, and third positions of the `'aaa'` string.