Here's the code that provides a self-contained solution to the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Count how many times a given substring can be found in the original string.

    :overlapping substring instances are counted  
    Return 0 if the substring is not found anywhere 
    """
    return sum(1 for _ in string.contains(substring))
```

This code defines a function that uses the `contains` method to iterate over all instances of a given substring in the original string. 
The function returns the number of times the substring is found, either by length or by case, depending on the input.