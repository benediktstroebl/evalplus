```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

#Test cases
verify_max_element([1, 2, 3])
verify_max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
verify_max_element([])
verify_max_element([-5, -3, -2, -10])
verify_max_element([1, 2, -3, 4, 5, 6, -1])
verify_max_element([[1, 2, 3], [4, 5, 6]])
verify_max_element([[1, 2, 3], [], [4, 5, 6]])
verify_max_element([[1, 2, 3], [1, 2, 3], [4, 5, 6]])
verify_max_element([[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]])
```
The above Python code defines a function `max_element` that calculates and returns the maximum element from a given list. It also includes a test cases to verify the correctness of the `max_element` function.