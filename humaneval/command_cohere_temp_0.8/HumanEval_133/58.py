```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest higher integer first.
    """
    result = sum(x**2 for x in lst if x % 1 == 0)
    return result
```

This approach directly uses the sum function to calculate the sum of squared values in the list. There are no unnecessary list comprehensions or extra variables introduced, making it efficient and readable. Also, since the sum function returns the sum of all elements in the list, including those that fail the condition, the filter condition is correctly placed outside the function.