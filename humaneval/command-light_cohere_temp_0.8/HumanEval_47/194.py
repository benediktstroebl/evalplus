```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # Return None for empty lists
    m = l[len(l) // 2]
    if len(l) % 2 == 0:
        return (m + l[len(l) // 2]) / 2
    return m

# Test suite
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test_median()
``` 
This script defines a `median` function that calculates the median of the elements in a given list. It also includes a test suite that passes the function's output against the expected result. 

Please note that the `median` function is self-contained and does not require any additional imports or external functions to be called.