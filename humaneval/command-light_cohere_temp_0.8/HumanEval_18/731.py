```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string, 
    including overlapping matches.
    Returns an number of total occurrences.
    >>> how_many_times('aaa', 'aa')
    3
    """
    return sum(1 for x in string.ic.find(substring, repeat=True)
    ```
```
This function uses the `findall()` method to count the occurrences of the substring in the original string. It iterates through loop and uses the `sum()` function to calculate the total number of occurrences.