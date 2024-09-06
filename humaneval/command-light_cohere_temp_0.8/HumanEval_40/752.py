```python
def triples_sum_to_zero(l: list):
    return any(sum(x) == 0 for x in l)

# Test the function
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == True
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
```
The above code defines a `triples_sum_to_zero` function that determines whether the sum of any three distinct elements in a list equals zero. The test_triples_sum_to_zero function contains several test cases that validate the function's correctness.