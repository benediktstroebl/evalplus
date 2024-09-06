```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns the number of occurrences of substring in string.
    """
    string = string.lower()  #
    string = ''.join(string)
    sub = substring.lower()

    string = ''.join(substring)
    count = 0
    for i in range(len(string)):
        if string[i] == sub:
            count += 1
    return count
```