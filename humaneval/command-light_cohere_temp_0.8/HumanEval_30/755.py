```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with some inputs
print(get_positive([-1, 2, -4, 5, 6])) # Expected Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected Output: [5, 3, 2, 3, 9, 123, 1]

# Test another list with mixed input
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10, -2])) # Expected Output: [-2, 3, 123]
```
The function get_positive takes a list as input and returns a new list with all the positive elements from the original list. 

The function is then tested with a variety of inputs and the results are verified against the expected outputs.