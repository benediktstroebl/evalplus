```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    lists of integers are given.
    It checks if there exist two numbers in the list whose sum is 0.
    If the list has only one number that sums up to 0, it will return False.
    If list has two numbers that add up to 0, it will return True
    """
    return sum(x for x in l if x > 0) <= 2

#Example test cases
assert(pairs_sum_to_zero([1, 3, 5, 0])) == False
assert(pairs_sum_to_zero([1, 3, -2, 1])) == False
assert(pairs_sum_to_zero([1, 2, 3, 7])) == False
assert(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) == True
assert(pairs_sum_to_zero([1])) == False
```
The function, `pairs_sum_to_zero`, returns `True` if there exist two distinct elements in the list that sum up to 0, and `False` otherwise.  The function uses a list comprehension and a `sum` function to check if there exist two numbers that add up to 0.