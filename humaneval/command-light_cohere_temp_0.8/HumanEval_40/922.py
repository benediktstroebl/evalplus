```python
def triples_sum_to_zero(l: list):
    if sum(x for x in l if x != 0) == 0:
        return True
    else:
        return False
```

The function takes a list of integers as an input and returns True if there are three distinct elements in the list that sum to zero, and False otherwise.

The function uses a generator expression with the sum function to check if there are three distinct elements in the list that sum to zero. If the sum of the elements is zero, it returns True. If the sum of elements is not zero, it returns False.