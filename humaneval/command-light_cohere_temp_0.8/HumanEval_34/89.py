```python
def unique(l: list):
    return list(set(l))

# Test case 1: succeeds
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
# expected output: [0, 2, 3, 5, 9, 123]

# Test case 2: succeeds
unique([1, 2, 3, 4, 5])
# expected output: [1, 2, 3, 4]

# Test case 3: succeeds
unique([1, 2, 3, 'x', 5])
# expected output: [1, 2, 3]

# Test case 4: fails, element 'x' is duplicate
unique([1, 2, 3, 'x', 5])
# error: ['x', 5] is duplicate
```