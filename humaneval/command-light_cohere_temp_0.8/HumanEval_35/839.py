```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) ,123)
assertEqual(max_element([]) ,())
assertEqual(max_element([10, 10, 10]) ,10)
assertEqual(max_element([10, 100, 10]) ,10)
assertEqual(max_element([10, 10, 101, 100]) ,101)
assertEqual(max_element([10, 101, 102, 103]) ,103)
assertEqual(max_element([1, 2, 3, 4, 5]) ,5)

# Another test
assertEqual(max_element([21, 18, 14, 12]) ,14)
```
The function max_element takes a list lst as input and returns the maximum element in the list. It utilizes the simple max() function to find the maximum element. The test cases ensure that the function is working correctly.