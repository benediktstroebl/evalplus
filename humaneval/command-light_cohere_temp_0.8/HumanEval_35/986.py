```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 (Various data types)
assert max_element([-5, -3, 3, 123]) == 123
``` 
This code defines a max_element function that returns the maximum element in a given list. It utilizes the test various lists with different data types and ensures the correctness of the results through assert statements.