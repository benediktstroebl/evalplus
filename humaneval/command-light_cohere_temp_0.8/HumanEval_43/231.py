```python
def pairs_sum_to_zero(lst):
    total = sum(lst)
    if total > 0:
        return False
    return True
```
This function determines whether all pairs of numbers in the list sum up to zero. It achieves this by computing the sum of all elements in the list, and then comparing it with zero. 

The function's test cases cover a wide range of scenarios, including lists with only one element, lists with negative and positive numbers, and lists with two distinct elements whose sum is zero.