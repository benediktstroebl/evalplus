```python
def max_element(lst):
    return max(lst)

# Test case 1
test_1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assertEqual(max_element(test_1), 123)

# Test case 2
test_2 = [5, 3, -5, 2, -3, 3, 9, -2, 1, -100]
assertEqual(max_element(test_2), -2)

# Test case 3
test_3 = [1, 2, 3, -10, -20]
assertEqual(max_element(test_3), 3)
```
The provided code defines a Python function max_element that calculates and returns the maximum element from a given list. It is tested by asserting that the function produces the correct results for three different test cases.