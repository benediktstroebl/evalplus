```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test the function with various list inputs
print(get_positive([-1, 2, -4, 5, 6])) # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function named `get_positive` designed to extract only the positive numbers from an input list. 

It utilizes a list comprehension technique with a conditional expression to filter and retain only positive integers from the provided list. 

The function is then tested with different input lists to validate its behavior and ensure correct output.