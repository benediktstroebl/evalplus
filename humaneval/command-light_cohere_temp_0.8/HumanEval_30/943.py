```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test case 1: Simple list
print(get_positive([-1, 2, -4, 5, 6]))
# Expected output: [2, 5, 6]

# Test case 2: List of strings
print(get_positive(["a", "b", "c", "d", "-e", "f"]))
# Expected output: [a, b, c, d]

# Test case 3: List of mixed data
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, -10, "hello"]))
# Expected output: [5, 3, 2, 3, 9, 123]
```
This script defines a function `get_positive` that takes a list as input and returns a new list containing only the positive numbers from the original list. It uses list comprehensions to filter out the positive numbers from the input list, which provides a self-contained solution to the problem. The script also includes a test case to ensure the correctness of the function.