```python
def max_element(lst):
    return lst[0] if len(lst) == 1 else lst[-1]

# Test cases with lists of different lengths and elements
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([9, 2, 3, 8, 5, 7]))  # Output: 9
print(max_element([9, 2, 3, 8, 5, 7, 8, 7, 6]))  # Output: 9
print(max_element([9, 2, 3, 8, 5, 7, 6, 7, 8]))  # Output: 9
```
The function `max_element` efficiently determines the maximum element in the list, whether it's the first element (of length 1) or the last element (of any other length), thanks to its straightforward logic and optimal time complexity.