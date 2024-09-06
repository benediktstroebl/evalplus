```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with some inputs
print(get_positive([-1, 2, -4, 5, 6]))  # Expected Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected Output: [5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function named `get_positive` that takes a single argument, `l`, which is expected to be a list. It uses list comprehension to iterate through list elements and check if each number is greater than or equal to zero, returning only the positive numbers. The function effectively filters out negative numbers from the input list and returns the modified list. 

The code then tests the `get_positive` function with a couple of inputs, printing the result to the console to ensure it is working as expected.