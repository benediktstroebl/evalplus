Here's the code you requested, which defines a function that determines the number of times a given substring appears in another string while avoiding duplicates:

```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a substring in the string, 
    while ignoring duplicates and case.
    >>> return sum(1 for s in string.find(substring, re.how_many_times)) 
    """

Example usage:
>>> how_many_times('aaa', 'a')
3
>>> how_many_times('aaaa', 'aa')
3
>>> how_many_times('abcde', 'abc')
2
>>> how_many_times('abcda', 'abcd')
3
```