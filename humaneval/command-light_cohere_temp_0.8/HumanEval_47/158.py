```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function
def test_median():
    # Sample list
    l = [-10, 4, 6, 1000, 10, 20]
    assert median(l) == 15.0  # "Median is 15.0"

   
# Error cases
    l = [3, 1, 2, 4, 5]
    assert median(l) == 5.0  # "Error, 3 is not in the list"
    l = [10, 20, 2, 0, 1]
    assert median(l) == 1.0  # "Error, 0 is out of range"
```