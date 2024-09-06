```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assertEqual(max_element([1, 2, 3]), 3)

# Test case 2
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) ,123)
```
The provided code defines a Python function max_element that takes a list lst as input and aims to return the maximum element in the list. The function uses the maximum function to achieve this, which returns the maximum value present in the list. 

The code also includes two test cases to verify the correctness of the max_element function. The first test case uses a list with integers [1, 2, 3], and the function correctly returns the maximum value 3. The second test case utilizes a list with a mix of values, including positive and negative numbers, and the function correctly identifies the maximum value as 123.