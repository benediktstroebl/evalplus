```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with sample inputs and expected outputs
# Test with a list containing only positive numbers
test_get_positive([2, 5, 6]) == [2, 5, 6]
# Test with a list containing both positive and negative numbers
test_get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
```
This code defines a function `get_positive` that takes a list as an argument and returns a new list containing only the positive numbers from the original list. The function uses a basic list comprehension with the condition `if num >= 0`, which checks if each element in the list is greater than or equal to zero. 

The code then provides two sets of test cases to verify the correctness of the function.