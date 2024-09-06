```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Tests
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 30, 100, 200]
    assert median(lst) == 15.0

# Example usage
test_median()
```