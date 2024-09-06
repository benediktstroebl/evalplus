```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    m = n // 2
    if n % 2 == 1:
        return (l[m] + l[m - 1]) / 2
    else:
        return l[m]

def test_median():
    """Function to test the median function."""
    assert median([3, 1, 2, 4, 5]) == 3.0

def test_median_list():
    """Function to test the median function with list of numbers."""
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```

The above code defines a `median()` function that calculates the median of a list of numbers. It also provides two functions, `test_median()` to test if the function is working correctly and `test_median_list()` to test the function with the list of numbers.