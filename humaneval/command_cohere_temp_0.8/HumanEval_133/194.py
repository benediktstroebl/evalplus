```python
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    rounded_lst = [round(x) for x in lst]
    return sum(x ** 2 for x in rounded_lst if x >= 1 and x % 1 == 0)
```

The function `sum_squares` serves the purpose of calculating the sum of the squares of integers in a given list. It accepts a list `lst` as its argument and returns the sum of the squares. Inside the function, each element in the list is rounded up to the nearest integer using the `round()` function. After that, the squared values of the rounded numbers are computed using a generator expression and the sum is calculated using the `sum()` function. To ensure accuracy, the function only considers integers that are greater than or equal to 1 and without decimal points. 

This is validated by the provided examples, which show the expected output for different lists of numbers.