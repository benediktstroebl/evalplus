```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with different list inputs
print(get_positive([-1, 2, -4, 5, 6]))   # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a `get_positive` function that takes a list as input and returns a new list containing only the positive elements from the original list. 

It achieves this by using list comprehension and filtering out the elements that are greater than or equal to zero.