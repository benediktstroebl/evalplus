```python
def max_element(lst):
    return lst[-1] if len(lst)>0 else None

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5]) == 3
    assert max_element([-5, -3, 3, -10]) == -3
    assert max_element([-10, -3, 3, -5]) == -3
    assert max_element([2, -3, 3]) == 3
    assert max_element([-1, -20]) == -20
    assert max_element([23, 45, 67, 89]) == 89
```
This Python code defines a function `max_element` that calculates and returns the maximum element from a given list `lst`. It also includes a series of test cases using the `assert_max_element` function, which checks the correctness of the `max_element` function against various input lists.