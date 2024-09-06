```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with some data
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

This function, `get_positive`, takes a list as an argument and returns a new list containing only the positive numbers from the input list. 

The function is designed to be self-contained, meaning it can be called and understood without further explanation, and it can be used in other parts of the program without needing external references. 

The function passes all the tests presented above, correctly identifying and returning only the positive numbers from the given lists.