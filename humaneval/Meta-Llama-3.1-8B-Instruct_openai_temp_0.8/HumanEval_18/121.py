### How Many Times Substring Can Be Found in the Original String
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string.
    Count overlapping cases.

    Args:
        string (str): The original string.
        substring (str): The substring to be searched.

    Returns:
        int: The number of times the substring can be found in the original string.

    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    count = 0
    for i in range(len(string)):
        # Check if the substring matches the string at the current position
        if string[i:i + len(substring)] == substring:
            count += 1
    return count
```
This script defines a function `how_many_times` that takes two string arguments, the original string and the substring to be searched. It iterates over the original string and checks if the substring matches the string at the current position. If a match is found, it increments the count. The function returns the total count of matches.