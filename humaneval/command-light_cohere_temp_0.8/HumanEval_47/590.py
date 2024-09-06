```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("Input list is empty, cannot compute median.")
    mid = len(l) // 2
    if len(l) % 2 == 1:
        return (l[mid] + l[mid - 1]) / 2
    else:
        return l[mid]

# Test suite
def test_median():
    input_list = [-10, 4, 6, 1000, 10, 20, 1, 2, 4]
    result = median(input_list)
    assert result == 15.0
    print("Test passed!")
```