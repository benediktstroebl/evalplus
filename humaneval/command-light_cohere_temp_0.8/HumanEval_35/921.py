```python
def max_element(lst):
    if not_positive(lst) and not_empty(lst):
        return lst[-1]
    elif not_empty(lst):
        return float('-inf')
    else:
        return float('inf')

def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123

def not_positive(lst):
    for x in lst:
        if x <= 0:
            return False
    return True

def not_empty(lst):
    return len(lst) == 0
```