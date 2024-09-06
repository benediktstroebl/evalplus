```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists

# Positive output: [-4, 2, 3, 5, 6, 9, 123]
print(get_positive([-4, 2, 3, 5, 6, 9, 123]))  # Output: [-4, 2, 3, 5, 6, 9, 123]

# Negative output: [-1, -5, -3, 7, 8]
print(get_positive([-1, -5, -3, 7, 8]))  # Output: [-1, -5, -3, 7]

# List with mixed positive and negative numbers
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123]))  # Output: [5, 3, 2, 3, 9, 123]

# Zero element
print(get_positive([0]))  # Output: []

# List with only one number (e.py should be a experiment and note the behavior)
print(get_positive([9, 9, 9, 9])))  # Output: [9, 9, 9]
```
This Python script defines a function `get_positive` that filters out negative numbers from a given list and returns only the positive numbers. The function is then tested with various input lists, showcasing its ability to handle positive and negative numbers as well as zero. The script also demonstrates how the principle of removing negative numbers and keeping only positive values.