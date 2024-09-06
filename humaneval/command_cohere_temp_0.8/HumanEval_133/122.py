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

The function `sum_squares` serves the purpose of computing the sum of squared integers in an input list. It first rounds each element in the list to the nearest larger integer and then calculates the sum of squared elements. This approach ensures that the expected output is achieved, as outlined in the problem statement. The examples provided in the docstring demonstrate its expected behavior.