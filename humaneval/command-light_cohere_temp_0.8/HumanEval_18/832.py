```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns the count of occurrences of the substring in the string.
    Args:
        string: str, the input string
        substring: str, the substring to search
    Returns:
        int, the count of occurrences of substring in the string
    """
    return _how_many_times(string, substring)

def _how_many_times(string, substring):
    count = 0
    i = 0
    while i < len(string) - 1:
        if string[i:i+len(substring)] == substring:
            count += 1
        i += 1
    return count
```