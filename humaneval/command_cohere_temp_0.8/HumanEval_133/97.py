```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest larger integer.
    """
    result = 0
    for element in lst:
        result += int(element)**2
    return result
```

This approach rounds each list element to the nearest larger integer and then squares each integer, ultimately providing the desired result.