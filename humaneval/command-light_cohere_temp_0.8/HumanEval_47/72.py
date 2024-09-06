```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test suite
def test_median():
    l = [-10, 4, 6, 1000, 10, 20]
    assert median(l) == 15.0

# Test passing large amounts of data
l = list(range(1001))
assert median(l) == 500.0

# Test passing different types of objects
l = [5, 2, "hello", [1,2,3]]
assert median(l) == 2.0

test_median()
``` 
This script defines a `median` function that computes the median of a list's elements. It also has a test suite that checks the function's output for various scenarios, such as an even number of elements, an odd number of elements, passing large amounts of data, and passing data of different types (integers, strings, lists).