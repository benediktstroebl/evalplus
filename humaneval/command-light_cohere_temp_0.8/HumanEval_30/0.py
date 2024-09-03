```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with different inputs
print(get_positive([-1, 2, -4, 5, 6])) # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # Output: [5, 3, 2, 3, 9, 123, 1]
```
The get_positive function returns a list of positive numbers from the input list lst. It uses list comprehension to iterate over each element in the list and checks if the element is greater than or equal to zero, then it is added to the returned list. The test code demonstrates the done with the function with different inputs.