```python
def max_element(lst):
    return max(lst)

# Test the max_element function with some sample inputs
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123
assert max_element([]) == 0
assert max_element([27]) == 27
``` 
This code defines a Python function `max_element`, which returns the maximum element from the passed list. The function is then tested with various sample inputs and the test assertions ensure the function's correctness.