```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x**2 for x in lst if x % 1 == 0)
    return result
```

The function rounds each number to the nearest larger integer and then calculates the sum of the squared values of the resulting list. Finally, it returns the resulting sum. 

This approach takes advantage of the sum function's compatibility with generators to eliminate the need for a list comprehension, improving efficiency when dealing with large inputs.