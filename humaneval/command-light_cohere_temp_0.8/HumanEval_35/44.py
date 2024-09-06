```python
def max_element(lst):
    return max(lst)

# Test the max_element function
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]) == 123
assert max_element([-10, -5, -3, -2]) == -3
assert max_element([-10, -5, -3, -20]) == -20

```
The code defines a function max_element that calculates the maximum element in a given list using the `max()` built-in function. It is also includes test cases to ensure the correctness of the `max_element` function.