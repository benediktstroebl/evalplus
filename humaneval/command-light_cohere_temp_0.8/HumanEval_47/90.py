```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return l[len(l)//2]
    return (l[len(l)//2 - 1] + l[len(l)//2]) / 2.0
```
def test_median():
    # List with odd length
    test_list = [1, 2, 3, 4, 5]
    assert median(test_list) == 3
    # List with even length
    test_list = [1, 2, 4, 6]
    assert median(test_list) == 5.0

test_median()