```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in set function to remove duplicate elements, and the built-in sort function to sort the unique elements. 

To ensure that the function meets the problem requirements, a example call to unique is provided. The example calls to unique with a list of integers [5, 3, 5, 2, 3, 3, 9, 0, 123] and the expected output [0, 2, 3, 5, 9, 123]. 

The function unique correctly solves the problem of returning a sorted list of unique elements from a given list. Let me know if you would like me to execute this code to test it!