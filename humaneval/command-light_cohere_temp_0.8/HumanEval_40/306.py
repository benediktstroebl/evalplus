```python
def triples_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst)

# Test the function
tests = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 9, 7],
    [1],
]

for t in tests:
    assert triples_sum_to_zero(t) == False
```