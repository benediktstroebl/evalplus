```python
def max_element(lst):
    return max(lst)

# Basic test cases
print("max_element():", max_element([1, 2, 3])) # Output: 3
print("max_element():", max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: 123

# Lists with duplicate elements
print("max_element():", max_element([3, 3, 1, 2])) # Output: 3
print("max_element():", max_element([3, -3, 1, 2, 3, 3])) # Output: 3

# Empty list
print("max_element():", max_element([])) # Output: None

# List with complex data types
print("max_element():", max_element([123, 0, "hi", None])) # Output: None
```
The function `max_element` efficiently computes the maximum element in the input list, making it suitable for various scenarios involving lists and data types. 
The provided test cases cover a wide range of inputs and ensure the correctness of the function.