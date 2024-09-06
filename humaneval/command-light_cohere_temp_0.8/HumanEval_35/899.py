```python
def max_element(lst):
    if not_elements(lst):
        raise ValueError("Input list is empty")
    return max(lst)

def test_max_element(test_lst):
    test_lst = [1, 2, 3]
    assert max_element(test_lst) == 3
    test_lst.set([5, 4, 5, 6, 7]
    assert max_element(test_lst) == 6
    test_lst.set([8, 8, -9, -10])
    assert max_element(test_lst) == -9
```
This code provides a max_element function that takes a list lst as input and returns the maximum element in the list. It also includes a test function that provides a set of test lists to verify the correctness of the max_element function.