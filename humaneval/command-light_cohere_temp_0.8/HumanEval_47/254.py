```python
def median(l):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("Input list must not be empty")
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
# Unit tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4, 5]) == 5.0
    assert median([10, 20, 30, 40, 25]) == 25.0
    assert median([1, 2, 20, 3, 4, 5]) == 5.0
```
This Python code defines a function `median(l)` that calculates the median of the elements in a list `l`. The function raises a `ValueError` if the list is empty, and returns the median for lists with an even or odd number of elements. This provides a testing functions to validate the correctness of the median function.