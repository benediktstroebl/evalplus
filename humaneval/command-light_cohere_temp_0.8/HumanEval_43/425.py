```python
def pairs_sum_to_zero(lst):
    if not set(lst) <= {0}:
        return True
    else:
        return False
```  This function takes a list lst as input and returns True if there are two distinct elements in the list that sum to zero, and False otherwise.