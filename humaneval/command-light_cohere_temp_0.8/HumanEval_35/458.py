```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    return max(lst)

def not_positive(lst):
    return any(x > 0 for x in lst)

# Unit tests
test_max_element = lambda: max_element([1, 2, 3]) == 3
test_not_positive = lambda: max_element([5, 3, -5]) == float('-inf')

print("Test Results:", test_max_element(), test_not_positive())
```
This script defines a function `max_element` that finds the maximum element in a list. It also has a test functions to ensure the function correctly handles cases with positive and negative numbers.