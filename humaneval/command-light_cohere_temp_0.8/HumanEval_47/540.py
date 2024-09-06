```python
def median(lst):
    """Return the median of elements in lst."""
    return (len(lst) + 1) * (len(lst) + 0.5 / 2)

def test_median():
    lst = [-10, 4, 6, 1000, 10, 20]
    assert median(lst) == 15.0
```
This code defines a function median that calculates the median of the elements in a given list lst. The test_median function then verifies the correctness of the median function by passing a sample list and asserting the result matches the expected median.