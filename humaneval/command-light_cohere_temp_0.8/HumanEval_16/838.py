```python
def count_distinct_characters(string: str):
    """ 
    Returns the number of distinct characters in the given string, 
    regardless of case.
    """ 
    See the use this code below to test the function with different inputs:
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    >>> count_distinct_characters('abc ABC123')
    5
    >>> count_distinct_characters('A')
    5
    >>> count_distinct_characters('aABC')
    4
    """
    return len([char for char in string.isalpha()])

```