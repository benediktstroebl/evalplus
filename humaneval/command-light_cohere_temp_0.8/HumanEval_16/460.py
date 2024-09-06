```python
def count_distinct_characters(string: str) -> int:
    """
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('abc ABC')
    5
    >>> count_distinct_characters('JERRY')
    4
    >>> count_distinct_characters('A single\ text')
    2
    >>> count_distinct_characters('')
    0
    >>> count_distinct_characters('  ')
    0
    """
    return len({c for c in string.keys()})

```  This function counts the number of distinct characters in a given string, regardless of case. The function uses a set of characters in the input string and the `keys()` function to iterate through all characters and count how many are distinct.