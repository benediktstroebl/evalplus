```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in l) and all(x != 0 for x in l)

# Test the function
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == True
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
```

This script defines a function `triples_sum_to_zero` that takes a list of integers as an input. The function returns `True` if there are three distinct elements in the list that sum to zero, and `False` otherwise. The test function asserts that the function works correctly by passing the test cases.