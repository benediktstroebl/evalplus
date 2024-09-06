```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding duplicates.
    """

    unique_count = {}
    for char in substring:
        unique_count[char] = string.find(char, unique_count.count(char) + 1)

    return len(unique_count)
    """
    return len(unique_count)
```