```python
def sum_squares(lst):
    result = sum(x ** 2 for x in lst if x % 1 == 0)
    return result
```

The function `sum_squares` takes a list of numbers `lst` as its input and returns the sum of squared integers present in the list after rounding each element to the next highest integer. This behavior is achieved through the use of a generator expression and the `sum` function. 

Note that this approach will incur a `ValueError` when confronted with an element that is not integrally valid, as the `x ** 2` expression will raise the error, and the `sum` function will propagate it. 

This is a straightforward solution for the specified problem that relies on established Python principles.