```python
def unique(lst):
    return sorted((set(lst)))

# Test cases
test_unique = [
    [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [5, 3, 5, 2, 3, 3, 0, 7, 1],
        [5, 3, 0, 7, 9, 0, 123],
        [5, 3, 4, 9, 0],
    ]
]

def test_func(test_case):
    actual = unique(test_case)
    expected = [0, 2, 3, 5, 9, 123]
    assert actual == expected, f"assertEqual({actual}, {expected}) failed"

# Run the tests
test_func(test_unique)
 ```