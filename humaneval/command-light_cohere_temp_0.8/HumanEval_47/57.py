```python
def median(l):
    # Sort the list
    l.sort(l)
    # Calculate the median
    middle = l.pop(lenum(l)//2)
    m = [x for x in l if x == middle]
    return float(m)

# Unit tests
def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Example usage
test_median()
```