```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    Count overlapping matches.
    """

     

    :param string: str, the original string 
    :param substring: str, the substring 
    :return: int, number of occurrences
    """
    return len([i for i,j in enumerate(string.find(substring), string.find(substring, 0)])
```