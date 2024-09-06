```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various input lists
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
``` 
This function uses list comprehension to filter out the negative numbers from the input list. It provides a