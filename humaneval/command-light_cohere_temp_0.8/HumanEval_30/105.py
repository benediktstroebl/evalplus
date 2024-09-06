```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with various inputs
print(get_positive([-1, 2, -4, 5, 6])) # Expected Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Expected Output: [5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function called `get_positive` that takes a list as an argument. The function iterates through each number in the list, and returns it if it's greater than 0. It provides a example test cases, passing various inputs to the `get_positive` function, and the expected output is a list containing only positive numbers. 

So, the output matches the expected results.