```python
def pairs_sum_to_zero(l):
    """
    returns True if there are two distinct elements in the list that sum to zero,
    and False otherwise.
    """
    list comprehension, and the `sum()` function to check if there exist two elements that sum up to zero.
    """
return any(x + y <= 0 for x,y in l)

test_function = lambda: pairs_sum_to_zero([1, 3, 5, 0])
test_function() #True
test_function() #False
test_function() #False
test_function() #True
```
The `pairs_sum_to_zero` function uses a list comprehension and the `sum()` function to check if there are two elements in the list that add up to zero. If the `any()` function returns True, then it means there are two distinct elements that sum to zero, and the function returns True. If the `any()` function returns False, then the function returns False.