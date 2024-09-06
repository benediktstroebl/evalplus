```python
def max_element(lst):
    if not_negative(lst):
        return max(lst)
    else:
        return -1

def test_max_element():
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst1) == 123

def test_max_element_empty():
    lst2 = []
    assert max_element(lst2) == -1

def test_max_element_negative():
    lst3 = [5, 3, -5, 2, -3]
    assert max_element(lst3) == -1

if __name__ == "__main__":
    test_max_element()
    test_max_element_empty()
    test_max_element_negative()
```

This script defines a function `max_element` that returns the maximum element from a list. The function also has tests to validate its behavior for different cases. The test cases help to cover different scenarios and ensure the function behaves as expected.