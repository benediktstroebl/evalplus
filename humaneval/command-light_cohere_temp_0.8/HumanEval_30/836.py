```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    positive = [num for num in input_list if num > 0]
    return positive

# Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Case 1: ", get_positive(input_list1))  # Output: [5, 3, 2, 3, 9, 123]

input_list2 = [5, 3, -5, 2, -3, 3, -123, 0, -9, -1]
print("Case 2: ", get_positive(input_list2))  # Output: [5, 3, 2, 3]

input_list3 = [-1, 2, -4, 5, 6]
print("Case 3: ", get_positive(input_list3))  # Output: [2, 5, 6]
```

This script defines a `get_positive` function that takes an input list and returns a new list with only the positive numbers. The function uses list comprehension and a conditional statement to filter the numbers in the list. This script also provides three test cases to ensure the correctness of the `get_positive` function.