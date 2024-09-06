```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The function `sum_squares` takes a list of items as input and returns the sum of squared positive integers in that list. The code first filters out elements that are not instances of integers or floats, and then checks if those elements are greater than or equal to zero. It then takes the filtered elements and sums their squares using a generator expression, finally returning the result.