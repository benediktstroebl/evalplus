```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x, x)
    return result

# Test the function with various lists
def test_unique():
    tests = [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
        [1, 2, 3, 4, 5, 6],
        ['a', 'apple', 'elephant', 'banana'],
        [['blub', 'bubble'], ['wuz', 'elephant']]
    ]

    for test in tests:
        actual = unique(test)
        expected = [0, 2, 3, 5, 9, 123]
        print(f"Test {test}: Actual ({actual}), Expected ({expected})")
        assert actual == expected, f"False - Actual: {actual}, Expected: {expected}"

# Run the test suite
test_unique()
 ```