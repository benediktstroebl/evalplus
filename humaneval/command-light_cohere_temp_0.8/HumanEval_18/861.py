```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, counting overlapping cases.
    >>> return sum(1 for x in string.find(substring, string))
    """
    return sum(1 for x in string.find(substring, string))
``` 

The function is self-contained and efficiently counts the occurrences of the substring in the original string. It utilizes the find() function to search for all occurrences of the substring and returns the total count.