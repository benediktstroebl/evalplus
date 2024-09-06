```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Return the number of times the given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')  == 3
    >>> how_many_times('aaaaaaa', 'aa') == 6
    >>> how_many_times('abcdeabcdeabcde', 'abcde') == 6
    """
    return len(string.find(substring))
```