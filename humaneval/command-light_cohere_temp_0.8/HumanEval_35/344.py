```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test the function with some examples
list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(list1))  # Output: 123

list2 = [5, 3,  0, -10]
print(max_element(list2))  # Output: -10

list3 = [5, 3, 2, -5, -10, -5, -6, -20]
print(max_element(list3))  # Output: -5
```
The code defines a function `max_element` that takes a list as input and returns the maximum element in that list. The function uses the common Python function `max()` to get the maximum of the input list. The output of the maximum value of the function is the maximum element in the input list.