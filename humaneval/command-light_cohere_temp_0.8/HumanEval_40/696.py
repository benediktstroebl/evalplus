```python
def triples_sum_to_zero(l):
    return any(sum(x) == 0 for x in l) and all(x != 0 for x in l)

test_triples_sum_to_zero = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 9, 7],
    [1]
]

result = triples_sum_to_zero(test_triples_sum_to_zero)
print(result)  # Output: True
```