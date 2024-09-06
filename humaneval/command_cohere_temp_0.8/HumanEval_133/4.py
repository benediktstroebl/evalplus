```python
def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each list element to the nearest integer.
    """
    result = sum(int(round(n)) ** 2 for n in lst)
    return result
```

The function `sum_squares` employs a list comprehension to iterate through each number in the input list `lst`. Before squaring, the number is rounded to the nearest integer using the `int` and `round` functions. The rounded number is then squared and added to the `result` variable. Ultimately, the function returns the `result`, providing the sum of squared numbers in the list after rounding each element to the nearest integer. 

This approach ensures that each number in the input list is rounded to the nearest integer before being squared and contributing to the sum, following the problem's requirements.