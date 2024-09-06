```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test the function
def test_median():
    """Function to test the median function"""
    lst = [-10, 4, 6, 1000, 10, 20, 1, 2, 3]
    assert median(lst) == 3.0
    print("Test passed!")
```