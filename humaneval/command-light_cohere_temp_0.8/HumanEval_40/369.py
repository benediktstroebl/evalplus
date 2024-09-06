```python
def triples_sum_to_zero(l: list):
    return sum([x for x in l if x not in set([0, x])]) == 0

def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) is False
assert triples_sum_to_zero([1, 3, -2, 1]) is True
assert triples_sum_to_zero([1, 2, 3, 7]) is False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) is True
assert triples_sum_to_zero([1]) is False
```
The `test_triples_sum_to_zero` function is defined to assert the output of the `triples_sum_to_zero` function for a series of test cases, passing in lists of different numbers and checking whether the function returns `True` or `False` accordingly.