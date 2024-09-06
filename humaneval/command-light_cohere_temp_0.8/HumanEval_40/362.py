```python
def triples_sum_to_zero(l):
    return all(sum(x) <= 0 for x in l)

#Test the function
def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
# Try the rest of test cases
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
assert triples_sum_to_zero([1, 2, 3, 7]) == False
assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
assert triples_sum_to_zero([1]) == False

```
Do you need assistance with anything else I can help you with?