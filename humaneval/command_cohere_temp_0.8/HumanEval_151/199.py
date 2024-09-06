```python
def double_the_difference(nums):
    odd_squares = sum(x**2 for x in nums if x % 2 and x >= 0)
    return int(odd_squares)
```

This function leverages Python's list comprehension and the `sum()` function to calculate the sum of squares of odd integers in the `nums` list that are not negative integers. Using the `int()` function ensures that the result is returned as an integer. 

The function returns 0 if the input list is empty, as specified in the problem statement.