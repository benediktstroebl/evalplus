```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    while ignoring case and keeping all occurrences.
    """
   
    simple `count` approach, we can iterate through each character in the original string and check if it's also in the substring. We can also sure that we need to consider case-insensitive matches, so we convert both the substring and the string to lowercase during the loop.

return: number of times the substring appears.
    """
    function uses the string and substring as input and returns the number of times the substring appears in the original string.

Example usage:
>>> how_many_times('aaaa', 'aa')
3
```