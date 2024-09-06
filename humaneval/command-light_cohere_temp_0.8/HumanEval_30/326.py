```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

#Test cases
test_get_positive = []
test_get_positive.py  = [ [-1, 2, -4, 5, 6], [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 2, 7, 8, 3]]

#Function testing
def test_func():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

#Run the test suite
test_get_positive = unittest.main()
test_get_positive.py(test_func)()
```  This script defines a function `get_positive` that takes a list and returns a new list containing only the positive elements from the original list. It also contains several test cases to ensure that the function works correctly.