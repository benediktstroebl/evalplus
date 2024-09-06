```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string, 
    while counting overlapping cases.
    """
    string, substring = substring.
    count = 0
    str.find(substring, string)

    while count < len(substring) and str.find(substring, string):
        count += 1
    return count
```