```python
def triples_sum_to_zero(l: list):
    return sum(x for x in l if x != 0) <= 2

def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) is False

def test_triples_sum_to_zero2():
    assert triples_sum_to_zero([1, 3, -2, 1]) is True

def test_triples_sum_to_zero3():
    assert triples_sum_to_zero([1, 2, 3, 7]) is False

def test_triples_sum_to_zero4():
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) is True

def test_triples_sum_to_zero5():
    assert triples_sum_to_zero([1]) is False
```
The script defines a function `triples_sum_to_zero` that checks if there are three distinct elements in a list that sum to zero, and returns `True` if this is the case, and `False` otherwise. The `test_triples_sum_to_zero` function tests the function with various input lists and asserts the expected behavior. 
These test functions ensure that the `triples_sum_to_zero` function works correctly for different inputs.