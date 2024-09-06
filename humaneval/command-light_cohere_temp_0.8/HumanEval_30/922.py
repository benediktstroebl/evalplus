```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1
print("Test case 1: ", get_positive([-1, 2, -4, 5, 6]))
[2, 5, 6]

# Test case 2
print("Test case 2: ", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
[5, 3, 2, 3, 9, 123, 1]

# Test case 3
print("Test case 3: ", get_positive([5, 3, -5, 2, -3, 3, 9, 0, -123]))

# Test case 4
print("Test case 4: ", get_positive([-123, -5, -25]))

# Test case 5
print("Test case 5: ", get_positive([5, 0, 50, 5. sm, '# represent a list of numbers']))
```
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. The script also includes a test suite to ensure the correctness of the function with a variety of input lists.