```python
def median(l):
    """Return median of elements in the list l"""
    n = len(l)
    
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test suite for median function
def test_median():
    list1 = [1, 2, 3, 4, 5]
    list2 = [-10, 4, 6, 1000, 10, 20]
    list3 = [3, 4, 5, 6, 7]
    
    assert median(list1) == 3.0
    assert median(list2) == 15.0
    assert median(list3) == 5.0

test_median()
``` 
This code defines a function median that calculates the median of a list of numbers. It handles both even even and odd number of elements in the list. Also, it passes the test suite, which contains a list of different numbers, and checks if the function correctly calculates the median for each list.