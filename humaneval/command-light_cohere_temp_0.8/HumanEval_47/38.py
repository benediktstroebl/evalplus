```python
def median(l: list):
    """Return median of elements in the list l."""
    return sorted([x for x in l])[-1] if len(l) % 1 == 0 else (l[len(l) // 2] + l[(len(l) - 1) // 2]) / 2

def test_median():
    """Function to test the median function."""
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```

This Python script defines a function median that computes the median of a list of numbers. The median function uses the sorting the list of elements and selecting the middle element (or average of two middle elements if the list has an odd number of elements), to compute the median. 
The test_median function tests the median function by passing a list of numbers with a known median, and asserts that the computed median matches the expected result.