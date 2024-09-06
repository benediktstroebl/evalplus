```python
def max_element(lst):
    return max(lst)

# Test the function with various inputs
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , 123)
assertEqual(max_element([-5, 3, -20]) , -20)
assertEqual(max_element([-20, -30, 40, 2, 5]) , 40)
assertEqual(max_element([1, 2, 3, 4, 5]) , 5)
assertEqual(max_element([]) , 0)
```
The provided code defines a function max_element that takes a list as input and returns the maximum element in the list. It achieves this by using the max() function with the list comprehension as input. The code then provides a test cases to verify the correctness of the max_element function.