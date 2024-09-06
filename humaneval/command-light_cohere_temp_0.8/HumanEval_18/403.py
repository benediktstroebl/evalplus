Here is a Python script that defines a function to find the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function to find how many times a given substring can be found in the original string.
    >>> how_many_times('abcde', 'd')
    3
    >>> how_many_times('abcdefgabcdef', 'abcdef')
    4
    >>> how_many_times('aa', 'a')
    0
    >>> how_many_times('aa', 'aa')
    2
    """

    return len([i for i,j in enumerate(string.find(substring)])
```