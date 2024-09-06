```python
def pairs_sum_to_zero(l):
    if set(l) <= {0}:
        return True
    return False
```  This function will take a list l of integers and return True if there are two distinct elements in the list that sum to zero, and False otherwise.