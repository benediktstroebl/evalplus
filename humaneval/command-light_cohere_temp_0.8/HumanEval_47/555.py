```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Tests
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0

if __name__ == "__main__":
    test_median()
```