Here is a self-contained Python script that defines a function to solve the problem of counting the occurrences of a given substring within a given string:

```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    6
    >>> how_many_times('abcde', 'abc')
    4
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```