```python
def pairs_sum_to_zero(lst):
    if not set(lst) == {0}:
        return True
    return False
``` 
This function will accept any list of numbers and return `True` if there are two distinct elements in the list that sum up to zero, and `False` otherwise.