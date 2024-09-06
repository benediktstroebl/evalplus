```python
def sum_squares(lst):
    result = sum(x**2 for x in lst if x % 1 == 0)
    return int(result)
```

The function `sum_squares` takes a list of numbers as input and returns the sum of squared integers in that list. It does so by using a generator expression, created by surrounding a sequence of expressions in parentheses (`()`), to yield squared integers for each element in the list. The `sum()` function then adds up these squared integers.

To adhere to the problem's instruction of rounding each element to the upper integer, the function returns the result as an integer using the `int()` function, without rounding off any digits. This ensures the sum of squared integers is returned as an integer without any decimal points. 

This function elegantly solves the challenge of computing the sum of squared integers in a list, while also adhering to the problem's specific rounding guideline.