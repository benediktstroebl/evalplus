```python
def how_many_times(string: str, substring: str) -> int:
    """
    This function accepts two parameters: a string and a substring.
    Returns the how many of occurrences of the substring in the original string, not counting duplicates.
    """
    
    # Do a loop to count the occurrences.
    Counter counts the
    unique occurrences.
    return len(Counter(substring, string))
    """
    
    # use collections.Counter to count the string occurrences
    Counter will count the occurrences of the substring in the string, but without duplicates.
    return Counter(substring, string)
    return len(Counter)
```
This solution uses the Counter class from the collections module to efficiently count the number of occurrences of a substring in a given string. It avoids duplicates by using Counter to count the unique occurrences of the substring in the string.