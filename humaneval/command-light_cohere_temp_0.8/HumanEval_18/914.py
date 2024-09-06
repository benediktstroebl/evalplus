Here's a self-contained Python function that finds the number of times a given substring can be found in the original string while avoiding overlapping occurrences:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count the number of occurrences of a given substring in the original string.
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaaaaa', 'aa')
    3
    >>> how_many_times('////////////', ' ##')
    7
    """
    count = 0
    start = 0
    end = string.find(substring, 0)
    while end != -1:
        start = end + 1
        count += 1
        end = string.find(substring, start) 
    return count
``` 

This function uses the `find()` function to locate the substring and then counts the number of non-overlapping occurrences.