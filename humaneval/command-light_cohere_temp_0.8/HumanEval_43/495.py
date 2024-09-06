```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    return any element in l[0] + any element in l[1:] <= 0
```

This solution is a standalone Python function that checks if there are two distinct elements in a list that add up to zero. It uses the time to iterate through list elements and checks for the sum of any two elements to be less than or equal to zero.

Here is a breakdown of the code:
- The function `pairs_sum_to_zero` takes a list of integers `l` as input and returns a boolean indicating whether there are two distinct elements in the list that sum to zero.
- The function uses the built-in `+` operator to calculate the sum of two elements in the list.
- The function then checks if the sum of any two elements is less than or equal to zero.

The test cases and their expected results are also provided, which can be used to test the function.