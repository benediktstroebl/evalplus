```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test the function with a range of inputs
for i in range(0,10):
    lst = [i, ] + incr_list(lst)
    assert lst == [i+1, ][:len(lst)] == [i+2] + [i+1] * len(lst) : "Assertion failed"

def test_incr_list():
    pass
```