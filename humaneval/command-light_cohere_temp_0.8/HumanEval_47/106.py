```python
def median(l: list):
    """Return median of elements in the list l."""
    if len(l) < 1:
        raise ValueError("Input list must have at least two elements")
    middle = len(l) // 2
    if l[middle] > l[middle - 1]:
        l[middle], l[middle - 1] = l[middle - 1], l[middle]
    median_value = (l[middle] + l[middle - 1]) / 2
    return median_value
# Test the function
try:
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([10, 10, 20]) == 10.0
    assert median([10, 20, 30]) == 15.0
    except:
        raise AssertionError("Median doesn't match the expected result")
```