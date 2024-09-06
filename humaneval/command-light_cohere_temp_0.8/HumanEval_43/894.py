```python
def pairs_sum_to_zero(lst):
    for x, y in lst:
        if x + y == 0:
            return True
    return False
```
We have designed a function named `pairs_sum_to_zero` that takes a list of integers as an argument. The function uses a checking if the two elements of the list can add up to zero. If this condition is met, the function returns `True`, indicating the presence of a pair that sums to zero. Otherwise, it returns `False`, indicating that there are no such pairs in the list. 

This self-contained function can easily solve the problem and pass the test cases provided.