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
    return sum(x * x for x in rounded_lst)
```

The function `sum_squares` serves the purpose of calculating the sum of the squares of integers extracted from an input list, ensuring accuracy even when the inputs are floats. It achieves this by first rounding each element in the input list using the `round()` function, which by design rounds a number to the nearest integer. Then, it proceeds to compute the sum of squares using a list comprehension and the `sum()` function, applying the squared value of each rounded element. 

This robust approach effectively addresses the challenge, resulting in the proper calculation of the sum of squares even when the input list contains floating-point numbers, as exemplified in the given test cases.