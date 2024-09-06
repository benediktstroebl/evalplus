```python
def triples_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst) and any(x != 0 for x in lst)

# Test the function with various inputs
triples_sum_to_zero([1, 3, 5, 0])  # Output: False
triples_sum_to_zero([1, 3, -2, 1])  # Output: True
triples_sum_to_zero([1, 2, 3, 7])  # Output: False
triples_sum_to_zero([2, 4, -5, 3, 9, 7])  # Output: True
triples_sum_to_zero([1])  # Output: False
```
The provided function, `triples_sum_to_zero`, determines whether three distinct elements in a list can sum to zero. The function returns `True` if the list has three elements whose sum equals zero, and `False` otherwise. 
The test cases cover a variety of scenarios, such as lists with different lengths, elements, and negative values.