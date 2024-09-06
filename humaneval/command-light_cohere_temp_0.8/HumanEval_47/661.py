```python
def median(l: list):
    """Return median of elements in the list l"""
    return (sorted(l)[len(l)//2]) if len(l) % 2 == 0 else (l[(len(l) - 1)//2] + l[len(l)//2])/2

def test_median():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
This Python code defines a function **median(l: list)** that calculates and returns the median of elements in the list "l". It uses a helper function test_median() that asserts the correctness of the median function for a list of numbers [-10, 4, 6, 1000, 10, 20].