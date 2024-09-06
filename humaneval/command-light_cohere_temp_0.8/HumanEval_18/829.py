```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    Count overlapping matches
   
    counts the using any position in the string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    >>> how_many_times('abcdeabc', 'abc')
    5
    >>> how_many_times('abcbaabcc', 'ab')
    3
    >>> how_many_times('dpjsfdpjsb', 'dpjs')
    3
    >>> how_many_times('abcdeabcba', 'abc')
    5
    >>> how_many_times('abcbaab', 'ab')
    2
    """
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count
```