```python
def max_element(lst):
    if not_decimal(lst):
        return float('inf')
    elif not_int(lst):
        return 0
    else:
        return max(lst)

def test_max_element():
    test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(test_list) == 123

def not_decimal(lst):
    try:
        float(lst)
        return True
    except ValueError:
        return False
``` 
This code defines a function max_element that finds the maximum element in a given list. It does this by checking if any element in the list is a float using the not_decimal function, returning inf if that's the case. If any element is not a float, it returns 0. The test_max_element function tests the max_element function with a test list and asserts that the result is correct. 
Finally, the not_decimal function is defined to check if an element is a float or not.