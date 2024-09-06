```python
def max_element(lst):
    if not_elements(lst):  # Check if empty
        return None
    max_val = max(lst)
    return max_val

def test_max_element():
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    got1 = max_element(lst1)
    assert got1 == 123  # First test passes
    lst2 = [5, 3, 2, -5, -50, 3, 9, 0, 123, 1, -10]
    got2 = max_element(lst2)
    assert got2 == -50  # Second test fails => should return None
```