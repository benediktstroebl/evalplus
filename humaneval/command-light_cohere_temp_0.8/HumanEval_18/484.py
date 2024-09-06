Here is a Python script that defines a function to solve the given problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> 'aaaaaa' == how_many_times('aaa', 'aa')
    True
    >>> 'hello' == how_many_times('hello', 'o')
    False
    """
    counter = 0
    for i in string:
        if i == substring:
            counter += 1
    return counter
```