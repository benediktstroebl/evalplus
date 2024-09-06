```python
def sum_squares(lst):
    """
    Return the sum of squared numbers in the given list,
    round each element in the list to the nearest larger integer first.
    """
    result = sum(x ** 2 for x in lst if isinstance(x, (int, float)) and x >= 0)
    return result
```

The function `sum_squares` employs a list comprehension to iterate over each element in the input list `lst`. For each element, it checks if it can be either int or float and if it is greater than or equal to 0, at which point it calculates the square of that element and adds it to the `result` variable employing the `sum` function. The function then returns the `result`.