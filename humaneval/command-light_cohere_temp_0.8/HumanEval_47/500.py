```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        m1, m2 = n // 2, n // 2 + 1
        return (lst[m1] + lst[m2]) / 2
    else:
        return lst[(n // 2) - 1]

# Test the function
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.6

# Another test
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
The provided Python script defines a function called **median(lst)** that calculates and returns the median of the elements in the input list lst. The test_median() function verifies the accuracy of the median function.