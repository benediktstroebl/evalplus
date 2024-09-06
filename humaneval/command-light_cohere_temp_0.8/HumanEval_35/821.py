```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test case 1
try:
    print(max_element([1, 2, 3]))
except TypeError as e:
    print(e)

# Test case 2
try:
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
except TypeError as e:
    print(e)

# Test case 3
try:
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123]  ))
except TypeError as e:
    print(e)

# Test case 4: Basic list
print(max_element([1, 2, 3, 4, 5]))

# Test case 5: List with fallback element (max)
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123], float('inf')) )

# Test case 6: Empty list
print(max_element([]))

# Test case 7: List with one element
print(max_element([1]))

# Test case 8: List with negative element
print(max_element([9, -1, 1]))
```

This script defines a function max_element that takes a list as an argument. It performs basic type checks to ensure the input is a list, and then uses the built-in max() function to return the maximum element in the list. The code also includes various test cases to ensure the function behaves correctly for different scenarios.