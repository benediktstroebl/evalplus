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
    capped_lst = [round(x) for x in lst]
    return sum(x * x for x in capped_lst)
```

The function `sum_squares` serves to calculate the sum of squared integers in an input list. It begins by creating a new list, `capped_lst`, using a list comprehension that rounds each number in the input list upward to the nearest integer. The sum of the squared elements in this adjusted list is then calculated using a generator expression accompanied by a `sum` function, and the resultant value is returned.

This approach ensures that all calculations are performed on integers, thus avoiding the potential for decimal point errors. It also simplifies the logic by applying the rounding action only once, at the element-level, rather than attempting to round the final sum.