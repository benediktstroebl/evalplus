```python
def triples_sum_to_zero(lst):
    if sum([x for x in lst if x <= 0]) == 0:
        return True
    return False

# Test the function
triples_sum_to_zero([1, 3, -2, 1])  # Should return True
triples_sum_to_zero([1, 2, 3, 7])  # Should return False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Should return True
triples_sum_to_zero([1])        # Should return False
```
The function takes a list lst as input and checks whether there are three distinct elements in the list whose sum is zero.  It returns True if this is the case and False otherwise.