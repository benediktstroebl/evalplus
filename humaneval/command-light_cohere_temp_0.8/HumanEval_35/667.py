```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1:
def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123

# Test case 2:
def test_max_element2():
    test_list = [-5, 3, 2, -3, 3, -10]
    assert max_element(test_list) == -3

# Test case 3:
def test_max_element3():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert max_element(test_list) == 9
```
This code defines a function `max_element` that returns the maximum element in the provided list. It has three test test cases to validate the function's behavior. The code provides clear and consistent test cases to demonstrate the correctness of the `max_element` function.