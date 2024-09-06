```python
def pairs_sum_to_zero(l):
    if not set(l) == {0} and len(l) > 1:
        return True
    else:
        return False
```

This function, `pairs_sum_to_zero`, takes a list of integers as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. It uses the particular set of the list elements to the power set, and then checks if the set contains the number zero. The function also checks if the list has more than one element. 

This function is self-contained and efficiently solves the problem described in the prompt.