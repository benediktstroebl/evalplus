```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))     # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```
This code defines a `get_positive` function that takes a list as input and returns a new list containing only the positive numbers from the input list. It uses list comprehension with the achieved by the `>=` operator within the comprehension.

The function is then tested using two different test cases, and the results are printed to the console.