```python
def max_element(lst):
    return lst[-1] if len(lst)>0 else None

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 123
    assert max_element([-5, -3, 3, -10]) == -3
```