Here is a self-contained Python function that solves the problem you described: 

```python
def how_many_times(string, substring): 
    """ 
    Returns the number of occurrences of the given substring in the 
    original string.
    """ 
    return sum(1 for c in string.find(substring, 0, string. + substring in string))
```