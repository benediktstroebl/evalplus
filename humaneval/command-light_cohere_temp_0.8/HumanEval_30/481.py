```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]

```
This script defines a function called `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses list comprehension to create this new list. The test cases demonstrate the the expected output of the `get_positive` function for different input lists.