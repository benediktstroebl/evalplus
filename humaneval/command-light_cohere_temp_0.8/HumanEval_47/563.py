```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("Input list must not be empty")
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test suite
for i in range(10):
    test_med = median([i, i+1])
    assert test_med == i+1

# Test with invalid input (list empty)
try:
    median([]).
except ValueError as e:
    assert str(e) == "Input list must not be empty"
```