```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1: Returns [2, 5, 6]
get_positive([-1, 2, -4, 5, 6])

# Test case 2: Returns list with all positive numbers
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Test case 3: Should not raise an error, as list is empty
get_positive([])
```
This code defines a function 'get_positive' that takes a list as an argument and returns a new list containing only the positive numbers from the original list. The test cases demonstrate the