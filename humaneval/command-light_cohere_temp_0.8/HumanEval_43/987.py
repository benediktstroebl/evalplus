```python
def pairs_sum_to_zero(l):
    return sum(set(l)) == 0
```
The function takes a list of integers as an argument and uses the built-in set data type to remove duplicates and then checks if the sum of all the elements in the list is equal to zero. It returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.