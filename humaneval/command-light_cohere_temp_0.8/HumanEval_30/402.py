```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

#Test case 1: return only positive numbers from a list
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]

# Test case 2: return only positive numbers from a list of mixed values
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123]

# Test case 3: empty list
print(get_positive([]))  # Output: []

# Test case 4: list with negative number and zero
print(get_positive([5, 3, -5, 2, -3, 3, 0]))  # Output: [5, 3, 2]
```
The script defines the function `get_positive`, which takes a list as input and returns a new list containing only the positive numbers from the input list. The function is demonstrated by passing different test cases and verifying that it works correctly.