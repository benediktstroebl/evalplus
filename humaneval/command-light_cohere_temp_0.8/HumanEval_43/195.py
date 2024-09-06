```python
def pairs_sum_to_zero(l):
    return any([x + y == 0 for x, y in zip(l, l[1:])])

# Test the function
test_result = pairs_sum_to_zero([1, 3, 5, 0])
test_result = test_result  # Convert to boolean

print("Test Result:", endswith(test_result))
```

This script defines a function `pairs_sum_to_zero` that determines whether the sum of any pair of elements in a list is zero. The test function also passes the