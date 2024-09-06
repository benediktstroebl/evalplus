```python
def max_element(lst):
    if not_decimal(lst):
        return float('inf')
    elif not_int(lst):
        return float('-inf')
    return max(lst)

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
    assert max_element([]) == 0
    assert max_element([10, 2, 20]) == 20
    assert max_element([5, -5]) == 5
    assert max_element([10, 99, -1]) == 99
    assert max_element([]) == float('-inf')

def not_decimal(lst):
    return any('.' in lst)
```
The code defines a function `max_element` that returns the maximum element in a list. This is with an test function to test the correctness of the `max_element` function. 
The `not_decimal` function checks if the list contains any decimal numbers and returns `True` if there are any, otherwise returns `False`.