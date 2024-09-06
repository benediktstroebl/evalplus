```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] += 1
    return l

# Test the function with some examples
test_incr_list = [
    [1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]
]

for item in test_incr_list:
    print(incr_list(item))
```