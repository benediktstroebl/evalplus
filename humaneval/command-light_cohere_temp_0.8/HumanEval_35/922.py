```python
def max_element(lst):
    if not_unique(lst) == False:
        return "Input list must be uniq"
    return max(lst)

def test_max_element():
    assert max_element([1, 2, 3]) == 3
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
    assert max_element([]) == 0
    assert max_element([1, 2, -1, -2]) == 1
    assert max_element([5, A, B]) == A
```
This Python code defines a function max_element that finds the maximum element in a list, and a test function test_max_element that verifies the max_element function's correctness with a set of input lists.  It ensures that the maximum element is unique in the list and the list is not empty, it returns an error message.