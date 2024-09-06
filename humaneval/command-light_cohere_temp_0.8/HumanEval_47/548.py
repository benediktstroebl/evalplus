```python
def median(l):
    """Return median of elements in the list l."""
    m = []
    for i in range(len(l)):
        if i == len(l) // 2:
            m.append(l[i])
        else:
            m.append(l[i] + m[len(m) - 1 - i])
    return sum(m) / len(m)
# Tests
def test_median():
    return median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
This script defines a function median that computes the median of a list of numbers, then implements a test function test_median that passes the function's output against the correct result for a sample list.