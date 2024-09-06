```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    elif len(lst) == 0:
        return float('-inf')
    else:
        return max(lst)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    assert max_element(test_list) == expected

def not_positive(lst):
    return all(value > 0 for value in lst)
```