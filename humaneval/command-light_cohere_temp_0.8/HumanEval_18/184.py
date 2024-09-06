```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    without overlapping.
    :param string: str, the input string
    :param substring: str, the substring to search for
    :return: int, the count of occurrences of the substring in the string
    """
    return sum(1 for x in string.contains(substring))
```
Do you require help with anything else?