Here is a self-contained Python function that solves the problem of finding the number of times a given substring can be found in the original string, while also handling overlapping cases:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string, 
    while handling overlapping cases.
    """
   
    number of occurrences = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            number_of_occurrences += 1
    return number_of_occurrences
```