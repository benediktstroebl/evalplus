```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test cases
test_incr_list = [
    [
        ( [],   ),
        ([1,2,3],),
        ([5,3,5,2,3,3,9,0,123],),
    ]

for test in test_incr_list:
    actual = incr_list(test)
    assert actual == [x + 1 for x in test],
    print(f"Test {test} passed!")
```