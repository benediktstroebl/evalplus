Here is a self-contained Python script that defines and executes a function to solve the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a substring in the original string.
    Return the how substring is passed as a parameter, and the string is 
    passed as a parameter by default.
    Return the count of occurrences of the substring.
    >>> how_many_times('aaa', 'aa')
    3
    """
    return len(string.find(substring))
```