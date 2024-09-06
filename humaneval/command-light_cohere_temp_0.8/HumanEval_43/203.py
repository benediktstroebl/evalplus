```python
def pairs_sum_to_zero(l):
    return any(x + y == 0 for x, y in zip(l, l[1:]))

# Test the function with known good inputs and known bad inputs
# Placeholder tests to demonstrate function usage
test_pair = [1, 3]
test_pairs = [1, 3, -2, 1]
test_large = [1, 2, 3, 7, 8, 9]

if test_pair in pairs_sum_to_zero:
    print("Passed test with", test_pair)
elif test_pairs in pairs_sum_to_zero:
    print("Passed test with", test_pairs)
elif len(test_large) == 1:
    print("Passed test with", test_large)
else:
    print("Failed")
```