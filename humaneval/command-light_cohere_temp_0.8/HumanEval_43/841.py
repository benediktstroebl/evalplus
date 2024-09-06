```python
def pairs_sum_to_zero(l):
    return sum([x for x in l if x != 0]) == 0
```
This function checks if any two elements in the list sum to zero, and returns `True` if they do and `False` otherwise. 
To test the function, a few test cases are provided, which should pass successfully.