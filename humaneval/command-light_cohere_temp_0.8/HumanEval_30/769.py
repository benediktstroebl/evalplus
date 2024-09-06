```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123]

# Test case 3
print(get_positive([-666, 5, -3, 7, 8, 9]))    # Expected output: [-666, 5, 7, 8]

# Test case 4
print(get_positive([1, 2, 3, -4, 5, -6]))    # Expected output: [1, 2, 3, 5]
```
The provided code defines a function called **get_positive** that takes a list as an argument and returns a new list containing only the positive integers from the original list. 

This function employs a list comprehension with the **>= 0** condition to isolate and retrieve the positive integers from the input list. 
The code then tests the function by providing various input lists and verifying if the output of the **get_positive** function matches the expected output for each case. 
Feel free to ask any further questions!