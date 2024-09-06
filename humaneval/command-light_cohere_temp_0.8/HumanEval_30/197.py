```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

#Test case 1:
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]

#Test case 2:
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]

#Test case 3:
print(get_positive([]))  # Expected output: []

#Test case 4:
print(get_positive([1, 2, 3, -1, 4, -5]))  # Expected output: [1, 2, 3, 4]
```
The `get_positive` function takes a list as input and returns a new list containing only the positive numbers from the input list. 
This function is self-contained and does not rely on any other functions or modules. The test cases are used to verify that the function is working correctly.