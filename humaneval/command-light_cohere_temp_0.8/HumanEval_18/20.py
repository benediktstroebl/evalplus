Here is a self-contained Python function that solves the problem of finding the number of occurrences of a substring within a given string:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string. 
    1 match means it how many times the
    :return int
    """
    return sum(1 for i,x in enumerate(string.find(substring)))
```
This function uses the `re.find()` function from iterates over all substrings and returns the count of all matches, including overlapping matches.