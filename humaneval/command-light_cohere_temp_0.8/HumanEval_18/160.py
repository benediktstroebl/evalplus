```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    counting overlapping cases.

    :param string: str, the input string
    :param substring: str, the input substring 
    :return: int, the count of substring occurrences 
    """
    return sum(1 for x in string.find(substring, 0). repeat: 2)
```