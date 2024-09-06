```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of occurrences of the substring in the string.
    """
    count = 0
    string = string.replace(substring)
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```