```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Unit tests
test_pairs_sum_to_zero = unittest.TestCase(list=[
    ([1, 3], False),
    ([1, -2], False),
    ([2, 4], True),
    ([1, 1])])

result = test_pairs_sum_to_zero()
print("Sum to zero:", result.result)
```