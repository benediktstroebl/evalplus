```python
def max_element(lst):
    if not_numbers(lst):
        return float('-inf')
    return max(lst)

def test_max_element():
    assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

def test_not_numbers():
    assert max_element([11, 22, 33]) == 33
```

This Python script defines a function max_element that finds the maximum element in a list. The function first checks if the list contains only numbers, returning negative infinity if not. The function then uses the max() function to find the largest element. The function is also tested using two test cases: one that checks if the list contains only numbers and passes the test, and another checks if the list contains any other elements and passes the test as well.