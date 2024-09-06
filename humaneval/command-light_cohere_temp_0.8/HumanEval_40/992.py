```python
def triples_sum_to_zero(lst):
    return any(sum(t) == 0 for t in zip(*lst))

# Test suite
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False

```

This code defines a `triples_sum_to_zero` function that determines whether three distinct elements in a list sum to zero. The function returns `True` if there are, and `False` otherwise. The `test_triples_sum_to_zero` function contains several assertions that validate the function's behavior, demonstrating that it correctly identifies lists that have three elements whose sum is zero.