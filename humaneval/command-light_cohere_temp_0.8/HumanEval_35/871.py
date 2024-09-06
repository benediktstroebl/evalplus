```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic positive integers
assertEqual([1, 2, 3], max_element([1, 2, 3]))

# Test case 2: Negative integers
assertEqual([5, -5, -3], max_element([5, -5, -3]))

# Test case 3: Positive and negative numbers
assertEqual([0, 123, -10], max_element([0, 123, -10]))

# Test case 4: Complex numbers
assertEqual([9, 2, -5], max_element([9, 2, -5, 0]))
```
The problem is solved by finding the maximum element in the list. The function max_element takes a list lst as input and returns the maximum element in the list using the max() function. The script also includes several test cases to verify the correctness of the max_element function.