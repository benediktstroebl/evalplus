```python
def pairs_sum_to_zero(l):
    return any([x+y <= 0 for x, y in zip(l, l[1:])])

# Test the function with some examples
test_result = pairs_sum_to_zero([1, 3, 5, 0])
test_result = pairs_sum_to_zero([1, 3, -2, 1])
test_result = pairs_sum_to_zero([1, 2, 3, 7])
test_result = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
test_result = pairs_sum_to_zero([1])

assert test_result == False
```