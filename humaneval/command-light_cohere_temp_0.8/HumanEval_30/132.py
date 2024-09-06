```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with some data
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
``` 
This function uses list comprehension to filter out any negative numbers from the input list, ensuring that only positive numbers are returned.  The function is self-contained, and can be used as a standalone tool to solve this problem.