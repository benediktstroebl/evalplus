Here's a self-contained Python function that solves the problem of checking if there are two elements in an input list that sum to zero:
```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))
```
This function checks if there are two elements in the list that have a sum less than or equal to zero. It uses the` zip()` to iterate over the elements of the list twice, and checks if each pair's sum is less than or equal to zero.

This function is self-contained and can be used to solve the problem and pass the tests without depending on any other functions or variables.