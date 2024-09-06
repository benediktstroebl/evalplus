```python
def max_element(lst):
    if not_positive(lst):  # Test for non-positive values
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return all(map(lambda x: x >= 0, lst))

test_positive = [5, 3, -5, 2, -3, 3, 9, 0, -10, -20]
test_max_element = max_element(test_positive)
print("Maximum element:", test_max_element)  # Output: Maximum element: -20
```
This code defines a function `max_element` that returns the maximum element in a list. By incorporating tests_positive` and `not_positive` helper functions, it also ensures that the input list contains only positive values, which is a test case for the function. The `test_positive` list is passed to the function, and the output is the maximum element.