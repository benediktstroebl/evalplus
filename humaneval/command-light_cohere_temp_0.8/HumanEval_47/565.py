```python
def median(l):
    """Return median of elements in the list l.
    return sorted(l)[len(l)//2] if len(l)<=1 else sorted(l)[len(l)//2]
    return sorted(l)[len(l)//2]

def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([7, -9, 10, -3, -2]) == (7+(-9))/2
    assert median([1, 2, 3, 4, 5]) == 3.0

test_median()
```
This Python code defines a function `median` that calculates the median of a list of numbers. It also provides a test function `test_median` with several assert statements to validate the correctness of the `median` function.  This test specific test cases demonstrate the expected behavior of the function, including calculating medians for various input lists.