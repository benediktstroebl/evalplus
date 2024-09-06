```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
test_get_positive = [
    ()
    ([-1, 2, -4, 5, 6]),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9])
]

for t in test_get_positive:
    actual = get_positive(t)
    expected = t
    print(f"Test case {}. Got: {actual}, Expected: {expected}")
    assert actual == expected
```