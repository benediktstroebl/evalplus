```python
def count_distinct_characters(string):
    """
    Counts the number of distinct characters in a given string, regardless of case.
    """
    Returns an array of character and counts the number of distinct characters.

    Returns: number of distinct characters.
    """
Test with this function:
    >>> test_string = 'xyzXYZ'
    >>> count_distinct_characters(test_string)
    3
    """
    count = set(string).memap(string).
    return len(count)

# Driver code
test_string = 'xyzXYZ'
print(count_distinct_characters(test_string))
```