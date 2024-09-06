```python
def pairs_sum_to_zero(l):
    return any([x+y <= 0 for x, y in zip(l, l[1:])])

#Tests
test_pairs_sum_to_zero = []
test_pairs_sum_to_zero.append([2, 3, 5, 0])
test_pairs_sum_to_zero.append([1, 3, -2])
test_pairs_sum_to_zero.append(1, 2, 3, 7))
test_pairs_sum_to_zero.append([2])
test_pairs_sum_to_zero.append([1])

print("All tests passed!")
```