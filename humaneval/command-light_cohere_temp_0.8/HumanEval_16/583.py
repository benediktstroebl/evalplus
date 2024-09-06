```python
def count_distinct_characters(string: str):
    """ 
    Returns the count of distinct characters in the given string, 
    ignoring case.

    >>> count_distinct_characters('abc') 
    3
    >>> count_distinct_characters('abc Abc') 
    3
    >>> count_distinct_characters('XYZ') 
    3
    >>> count_distinct_characters('XYZabc') 
    3
    >>> count_distinct_characters(' jerry') 
    4
    >>> count_distinct_characters('abcXYZ') 
    2
    """
    return len(set(string.lower()))
```  This code defines a Python function that computes and returns the count of distinct characters in a given string, irrespective of their case. The function uses the particular string, then converts it to lowercase using `string.lower()` and subsequently uses the unique characters from the string using `set()` and the `len()` function to determine the count of distinct characters.