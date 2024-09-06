Here is a Python script that includes a self-contained function that solves the problem of counting the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string, 
    considering overlapping cases.
    >>> how_many_times('aaa', 'a') - 3
    0
    >>> how_many_times('aaaaaaa', 'aa')
    6
    """
    if substring not in string:
        return 0
    
    occurrences = []
    start, end = 0, 0
    len_substring = len(substring)
    
    while start < len_substring:
        end = start + 1
        if string[start:end] == substring:
            occurrences.append(end[end-1]
        start = end + 1
    
    return len(occurrences)
```