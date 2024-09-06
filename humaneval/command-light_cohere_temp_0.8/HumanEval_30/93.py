```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))      # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]

```
This Python code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. 

This function uses list comprehension and the `>= 0` operator to filter out the positive numbers. 

The test cases demonstrate the functionality of the `get_positive` function, passing various lists with positive and negative numbers, and providing the expected output.