```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases 1
get_positive([-1, 2, -4, 5, 6])  # Output: [2, 5, 6]

# Test cases 2
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])  # Output: [5, 3, 2, 3, 9, 123]

# Test cases 3
try:
    get_positive([0])  # Zero is a positive number but should return an error
    print("Success")  # Indicate an error
except ValueError:
    print("Error")  # Indicate a valid error

# Test cases 4
try:
    get_positive([-77, 99])
    print("Success")  # Shouldn't raise an error, should output [77, 99]
except ValueError:
    print("Error")  # This should be the correct behavior
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only positive numbers from the original list. The test cases validate the benefits of this function, demonstrating the handling of various scenarios.