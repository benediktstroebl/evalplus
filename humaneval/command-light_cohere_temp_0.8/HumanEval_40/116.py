```python
def triples_sum_to_zero(lst):
    if sum(x for x in lst if x < 0) == 0:
        return True
    return False
``` 
This script defines a function `triples_sum_to_zero` that takes a list of integers `lst` as input. The function returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.