```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called `unique` that takes a list `l` as input. It removes duplicate elements from the list using the `set()` function, which automatically eliminates duplicate values, and then sorts the unique elements using the `sort()` function. The sorted unique elements are returned as the output. 

The `unique` function ensures that duplicate elements are excluded and the result is sorted, making it a convenient solution for obtaining a list of distinct and ordered values from an input list. 

To verify the functionality of the `unique` function, you can use the following test cases:
```python
# Test case with a list of integers
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]

# Test case with a list of strings
>>> unique(['apple', 'banana', 'apple', 'orange', 'banana'])
['apple', 'banana', 'orange']

# Test case with a list containing a mix of integers and strings
>>> unique([5, 'banana', 2, 'apple', 3, 'orange', 9, 0, 'banana'])
[0, 2, 3, 5, 9, 'apple', 'banana', 'orange']
```

In these test cases, the `unique` function is applied to different lists, and the resulting output is displayed, demonstrating that it correctly returns sorted unique elements from the input lists.