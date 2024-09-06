```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = []
test_max_element.py: [1, 2, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
test_max_element.res: [float('inf'), -1e9]
test_max_element.py=[-11, -1e11]
test_max_element.py=[-7e7e]
test_max_element.py=[1e1e, -1e+100]
test_max_element.py=[1, 2, -500, 1e-100]

def test_function(test_case):
    """Unit tests"""
    max_element = max_element(test_case)
    assert max(test_case) == max_element

test_max_element = [test_function, test_max_element]
```