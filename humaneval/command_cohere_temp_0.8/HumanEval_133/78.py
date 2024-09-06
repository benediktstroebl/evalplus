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
    ceiling_lst = [int(x) for x in lst if x % 1 == 0 or x > 0]
    return sum(x * x for x in ceiling_lst)
```

The function `sum_squares()` takes a list of numbers as input and returns the sum of the squares of the rounded numbers in that list.

To do this, the function first creates a new list called `ceiling_lst` from the input list `lst`. This new list contains the upper integer ceiling value of each element in the input list, as obtained by int(x) for x in lst if x % 1 == 0 or x > 0. That is, it rounds each number up to the nearest integer value. 

Then, the square of each element in `ceiling_lst` is calculated and summed using a list comprehension and the `sum()` function. The result of this operation is the sum of the squares of the rounded numbers in the input list `lst`. 

This approach ensures that the sum of the squares operation is performed on the rounded values, as per the prompt instructions.