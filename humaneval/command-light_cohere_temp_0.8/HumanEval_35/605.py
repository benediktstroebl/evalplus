```python
def max_element(lst):
    if not_num(lst) == None:
        return None
    return max(lst, key=len)

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, 3, -10]) == 3
    assert max_element([5, 0, 123, 1, -10]) == 123
```
The provided code defines a function `max_element` that calculates the maximum element in a list, using the `max()` function along with the `key=len` parameter to order the list by the length of its elements. The `test_max_element` function contains several test cases that validate the correctness of the `max_element` function.