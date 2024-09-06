```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

#Test case 1:
print("Case 1:", get_positive([-1, 2, -4, 5, 6]))
#Expected output: Case 1:[2, 5, 6]

#Test case 2:
print("Case 2:", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
#Expected output: Case 2:[5, 3, 2, 3, 9, 123, 1]

#Test case 3:
print("Case 3:", get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -100]))
#Expected output: Case 3:[5, 3, 2, 3, 9, 123, 1]
```
This Python code defines a function named `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses ay list comprehension and the built-in function to achieve this. The function is then passed through various test cases, and its output is verified against the expected results, ensuring the correctness of the function.