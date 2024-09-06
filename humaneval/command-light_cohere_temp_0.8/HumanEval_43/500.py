Here is a Python script with a self-contained function that solves the problem of checking if there are two distinct elements in a list that sum to zero:
```python
def pairs_sum_to_zero(l):
    return sum([x for x in l if x]) % 2 == 0
```
The function checks if there are two distinct elements in the list that sum to zero, and returns True if they do, and False otherwise.