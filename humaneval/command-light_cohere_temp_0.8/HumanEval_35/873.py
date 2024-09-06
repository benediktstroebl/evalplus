```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test the function with some samples
#Test case 1:
test_case = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case) == 123

#Test case 2:
test_case2 = [5, 3, -5, 2, -3, 3, 9, 0, -100]
assert max_element(test_case2) == -100 

#Test case 3:
test_case3 = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert max_element(test_case3) == -5 
```
The function `max_element` uses the built-in Python `max` function to find the maximum element in the input list.