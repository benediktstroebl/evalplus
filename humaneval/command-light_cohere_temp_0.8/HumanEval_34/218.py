```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and not seen.

# Test cases
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)  # expected output: [0, 2, 3, 5, 9, 123]

test_unique2 = unique([3, 2, 5, 6, 9])
print(test_unique2)  # expected output: [2, 3, 5, 6, 9]

test_unique3 = unique([1, 2, 3, 4, 5, 6])
print(test_unique3)  # expected output: [1, 2, 3, 4, 5]
```