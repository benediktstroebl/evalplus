```python
def triples_sum_to_zero(lst):
    """
    Returns True if the list has three distinct elements that sum to zero, 
    and False otherwise.
    """
    triple = ([x, y, z] for x, y, z in lst if x + y + z == 0)
    if not triple: return False
    for x, y, z in lst:
        if x + y + z != 0: return False
    return True

# Example usage
lst = [1, 3, 5, 0]
result = triples_sum_to_zero(lst)
print(result)
```
The code will check if there are three distinct elements that sum to zero in the list. If the list has three such that are, then it returns True. Otherwise, it returns False.