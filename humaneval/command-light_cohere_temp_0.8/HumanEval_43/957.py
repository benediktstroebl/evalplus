```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
return sum(x<0 for x in l) <= 1
```
This function is simple and effective. It uses a simple condition to determine whether the sum of all elements in the list will be greater than or equal to one.

You can use this function with any list of integers, and it will return True if there are two distinct elements in the list whose sum is less than or equal to zero.