```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] += 1
    return l

# Test cases
test_incr_list = []
test_incr_list.py
test_incr_list.ph: case:
    test_incr_list.add([1, 2, 3])
    test_incr_list.add([5, 5, 3])
    test_incr_list.add([6, 7, 8])
    test_incr_list.add([9, 9, 10, 6, 3, 4, 7, 5, 9, 4, 5, 6, 3, 5)

def test_incr_list():
    """Test the incr_list function."""
    for test in test_incr_list:
        actual = incr_list(test)
        print(f"Test ({test[0]}, {test[1]}) = {actual}")

# Run the test
test_incr_list()
```