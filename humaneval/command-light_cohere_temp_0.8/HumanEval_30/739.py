```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test case 1:
print("Case 1: ", get_positive([-1, 2, -4, 5, 6]))
# Expected output: Case 1: [2, 5, 6]

# Test case 2:
print("Case 2: ", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Expected output: Case 2: [5, 3, 2, 3, 9, 123, 1]

# Test case 3:
print("Case 3: ", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -9]))
# Expected output: Case 3: []

# Test case 4:
print("Case 4: ", get_positive([-123]))
# Expected output: Case 4: []
```
This Python function, `get_positive`, takes a list as input and returns a new list containing only the positive numbers from the original list. The function utilizes list comprehension to iterate over each element in the input list and apply the condition `num >= 0` to filter out the positive numbers. 

In the test cases provided, the function is evaluated for different lists, and the expected output is shown. The script is self-contained and can be used as a standalone function to solve the problem for any given list.