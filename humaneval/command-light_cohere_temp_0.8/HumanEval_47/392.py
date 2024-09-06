```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    m = n // 2 + 1
    if n % 2 == 1:
        return (lst[m - 1] + lst[m]) / 2
    else:
        return lst[m]

def test_median():
    """Test the median function."""
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```

This Python code defines a function called median that calculates the median of a list of numbers. The median is the middle value of a sorted list, which divides the list into two even halves. 

The code then provides a function called test_median which tests the correctness of the median function using a predefined list of numbers.