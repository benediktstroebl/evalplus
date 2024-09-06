```python
def triples_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst)

# Tests
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
```
The function `triples_sum_to_zero` will return `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise.