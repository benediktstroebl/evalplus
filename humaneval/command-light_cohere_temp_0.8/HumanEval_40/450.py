```python
def triples_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst)

# Test cases
tests = [
    [1, 3, 5, 0], returns=False, 
    [1, 3, -2, 1], returns=True, 
    [1, 2, 3, 7], returns=False, 
    [2, 4, -5, 3, 9, 7], returns=True,
    [1], returns=False,
]

for test in tests:
    assert triples_sum_to_zero(test) == test[returns]
```