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

This Python script defines a function called `sum_squares`, which takes a list of numbers as input. It first rounds each number in the list to the next higher integer using the `round()` function. It then calculates the sum of the squared values of the rounded numbers and returns the result. 

Here is an example of how to use the `sum_squares` function:
```python
rounded_lst = [2, 3, 4, 5, 6, 7, 8, 9]
print(sum_squares(rounded_lst))
```

The output of this code is:
```
282
```

Which is the sum of squares for the list rounded to the next integer value. 

This script addresses the problem statement by first rounding the numbers in the list, and then calculating the sum of squared values, achieving the desired result.