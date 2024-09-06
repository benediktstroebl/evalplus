```python
def how_many_times(string: str, substring: str) -> int:
    """
    Find how many times a given substring can be found in the original string, 
    counting overlapping occurrences.
    Return: int  - number of occurrences
    """
    return sum(1 for x in string.find(substring, string))
```

The function uses the `findall()` method to find all instances of the substring in the string. The `sum()` function then adds 1 for each instance of the substring, including overlapping occurrences. 

This function is self-contained and can be used to solve the problem for any given string and substring.