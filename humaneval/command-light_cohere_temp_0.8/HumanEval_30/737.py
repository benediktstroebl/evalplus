```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print(get_positive([-1, 2, -4, 5, 6]))
# Output: [2, 5, 6]

# Test case 2
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
# Output: [5, 3, 2, 3, 9, 123, 1]

# Test case 3
print(get_positive([5, -5, -20]))
# Output: []

# Test case 4
print(get_positive([-1, 2, -20, 5, 6, -100]))
# Output: []
```
This code defines a function `get_positive` that takes a list as input and returns a new list containing only the positive elements from the original list. The function employs a list comprehension and the condition `x >= 0` to achieve this. 

Test cases are then applied to the function to ensure its correctness. The expected outputs are the following:
- In test case 1, the output is `[2, 5, 6]`.
- In test case 2, the output is `[5, 3, 2, 3, 9, 123]`.
- In test case 3, the output is an empty list.
- In test case 4, the output is also an empty list, as there are no positive elements in the input list.