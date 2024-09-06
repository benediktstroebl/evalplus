```python
def pairs_sum_to_zero(l):
    return sum(x) < 0 for x in l if set(l) != set()

```

The above code checks if there are two distinct elements in the list that their sum is equal to zero, and returns `True` if that condition is met, and `False` otherwise. This is self- interesting function to solve this problem without using any external functions.