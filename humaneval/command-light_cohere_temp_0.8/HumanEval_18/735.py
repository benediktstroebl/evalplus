```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring within the original string, 
    while avoiding overlapping occurrences.
    >>>>>> how_many_times('aaa', 'aa')
    3
    """
    count = 0
    start = 0
    end = string.find(substring, -1)
    while end != -1:
        start = end + 1
        count += 1
        end = string.find(substring, start)

    return count
```