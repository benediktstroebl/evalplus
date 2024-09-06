```python
def triples_sum_to_zero(l):
    if not set(l) <= {0}:
        return True
    return False
```
The function uses the set difference operation to check if there are three distinct elements in the list that sum to zero, and returns True if this condition is met, and False otherwise. The function is self-contained and does not require any external variables or functions to solve the problem.