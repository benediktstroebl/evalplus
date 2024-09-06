```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("Input list must have at least two elements.")
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test suite
for i in range(0, 10):
    try:
        test_list = [i, i] + median([-10, 4, 6, 1000, 10, 20, i])
        assert median(test_list) == i + 10
    except AssertionError as e:
        print(f"Test failed at index {i}: {e}")

test_list = [-10, 4, 6, 1000, 10, 20] + median([-10, 4, 6, 1000, 10, 20])
print("Here is the output of the test suite:")
```