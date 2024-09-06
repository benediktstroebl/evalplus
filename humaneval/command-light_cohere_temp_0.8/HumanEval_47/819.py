```python
def median(l: list):
    """Return median of elements in the list l"""
    m = l[len(l) // 2] + l[len(l) // 2 - 1]
    return m

# Test cases
def test_median():
    """Function to test the median function"""
    lst = [-10, 4, 6, 1000, 10, 20, 2, 3, -20]
    assert median(lst) == 15.0
    print("Test successful!")

# Run the function and test
test_median()
```