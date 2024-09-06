Here is a self-contained Python script that defines and implements the function how_many_times to solve the problem you provided:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    3
    """
    return len({i:True for i, char in enumerate(string) if char == substring})
```