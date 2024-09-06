```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x + 1) % 2)

# Test suite for the function
test_suite = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [7, 8, 3]
]

for test in test_suite:
    actual = sort_even(test)
    expected = [3, 6, 5, 4]
    assert actual == expected, "Test failed: " + str(test)

print("All tests passed!")
```