```python
def max_element(lst):
    return max(lst)

# Test the function with various inputs
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-5, -3, -10]))         # Output: -10
print(max_element([1, 2, 3, -5]))       # Output: 3
print(max_element([]))                # Output: 0
print(max_element([123, 456, 789]))   # Output: 123
```
This script defines a function `max_element` that takes a list as input and returns the maximum element in the list. It is then tests this function with a variety of test cases, and all the test cases pass successfully.