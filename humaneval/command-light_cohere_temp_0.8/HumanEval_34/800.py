```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and not seen.

# Test cases
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test 1:", test_unique)  # Expected output: [0, 2, 3, 5, 9, 123]

test_unique = unique([])
print("Test 2:", test_unique)  # Expected output: []

test_unique = unique([1, 2, 3, 4, 5, 6])
print("Test 3:", test_unique)  # Expected output: [1, 2, 3, 4, 5]

test_unique = unique([10, 11, 12, 13, 14])
print("Test 4:", test_unique)  # Expected output: [10, 11, 12, 13, 14]
```

This script defines a function `unique` that returns a list of unique elements from the input list `l`. It uses a set `seen` to keep track of the unique elements encountered. The function iterates through each element from the input list `l` and adds it to the `seen` set if it's not already present and the current value is not seen.