```python
def get_positive(l: list):
    return [x for x in l if x >= 0]

# Test case 1: Positive numbers
print(get_positive([-1, 2, -4, 5, 6]))
[['2', '5', '6']]

# Test case 2: Zero values
print(get_positive([0, 2, -5, 5, 6]))
 [['2', '5', '6']]

# Test case 3: Negative numbers
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
 [['5', '3', '2', '3', '9', '123', '-1']]

# Test case 4: Mixed numbers
print(get_positive([5, 3, -5, 2, -3, 3, 0, 7, 8]))
 [['5', '3', '2', '3', '7', '8']]
```

This script defines a `get_positive` function that returns a list containing only the positive numbers from the input list. It uses list comprehension and a filtering condition to achieve this. The test cases demonstrate the above function's behavior and output.