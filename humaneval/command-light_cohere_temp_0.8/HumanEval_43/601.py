```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
test_result = test_result
test_result = test_result is False

print("Test results:", test_result)
```