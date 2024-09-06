Here is a self-contained Python script with a function that solves the problem you described:
```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the number of occurrences of a given substring in the original string, 
    taking into account overlapping occurrences.
    >>> 'abc' -> 'a' 
    """
    if not substring:
        return 0

    s = set(string)
    n = 0
    for x in s:
        if x == substring:
            n += 1

    return n
``` 
This script defines a function that takes two parameters: string and substring. It returns the responsible function that checks if the given substring is not empty and creates a set of characters in the string. Then, it iterates through the set to find the occurrences of the substring.