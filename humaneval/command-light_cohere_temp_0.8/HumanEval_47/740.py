```python
def median(l: list):
    """Return median of elements in the list l."""
    m = l[len(l) // 2] + abs(l[len(l) // 2] - l[len(l) - 1])
    return m

def test_median():
    """Function to test the median function."""
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test_median()

# Run the tests.
test_median()
```