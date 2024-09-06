```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    >>> how_many_times('aaa', 'a')    # [0, 3]
    >>> how_many_times('aaaa', 'aa')  # [3, 2]
    """

    # Sliding window for better performance
    window = set()
    count = 0

    for char in string:
        if char == substring:
            count += 1
        window.add(char)

    return count
```