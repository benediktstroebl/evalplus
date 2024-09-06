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

This Python script defines a function called `sum_squares`, which takes a list of numbers as input. Inside the function, it first rounds each element in the input list to the nearest larger integer using the `round()` function. These rounded values are then stored in a new list called `rounded_lst`. Following this, it calculates the sum of squared values from the `rounded_lst` list using a list comprehension and the `sum()` function, which is then returned as the result. 

This function is useful for calculating the sum of squared integers in a given list, ensuring that each number is rounded up to the nearest higher integer before squaring.