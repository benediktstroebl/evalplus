```python
def median(l):
    """Return median of elements in the list l"""
    return (sorted(l) + [0])[len(l) // 2]

# Test
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
``` 
The provided Python script defines a self-contained function, median, that computes the median of the elements in a given list. The function achieves this purpose using a method that constructs a list containing the median value and all elements of the original list. The test_median function is also defined to verify the correctness of the median function by passing a test list.