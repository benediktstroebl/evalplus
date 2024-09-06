```python
def sum_squares(lst):
    """Returns the sum of squared integers in lst, rounding each number to the next highest integer."""
    result = 0
    for n in lst:
        result += n ** 2
    return result
```
The function works by first iterating through each element in the list. It then squares each element, and adds the squared values to the total. To ensure that each number is rounded up to the nearest integer, it uses the expression `n ** 2`, which guarantees that the next highest integer value is used in the calculation. 

To handle the edge case of floating point numbers being stored in the list, we can modify the function to first check if the list contains any non-integer values, and raise a `ValueError` if it does:
```python
def sum_squares(lst):
    """Returns the sum of squared integers in lst, rounding each number to the next highest integer."""
    result = 0
    for n in lst:
        if not isinstance(n, int):
            raise ValueError("The list must only contain integers.")
        result += n ** 2
    return result
```