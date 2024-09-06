```python
def max_element(lst):
    if not_float_list(lst) or not _int_list(lst):
        raise TypeError("Input list must contain only integers or floats")
 
    return max(lst)

def test_max_element():
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    expected = 123
    assert max_element(lst) == expected

def _int_list(lst):
    return all(isinstance(i, int) for i in lst)

def _float_list(lst):
    return all(isinstance(i, float) for i in lst)

# Run the tests
test_max_element()
```
This script defines a function max_element that takes a list as input and returns the maximum element in the list. The function uses the testmax_element() to test the correctness of the max_element() function with a sample input list. The test checks if the maximum element is calculated correctly. Finally, the test_max_element() function is used to validate the correctness of the max_element() function.