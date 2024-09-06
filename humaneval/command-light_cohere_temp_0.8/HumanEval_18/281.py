Here's the code you asked for:
```python
def how_many_times(string, substring):
    """ Find how many times a given substring can be found in the original string, counting overlapping cases.
    >>> How many times does 'aa' in 'aaaa':
    3
    >>> How many times('aaaa', 'aa')
    3
    >>> How many times('abcdaabcda', 'abc')
    3
    >>> How manytimes('abcdaabcdaabc', 'abc')
    0
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```