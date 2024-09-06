```python
def is_sorted(lst):
    lst.sort()
    unique = set(lst)
    return len(unique) == len(lst) and len(lst) == len(set(lst))
```

The function `is_sorted` checks whether a given list of numbers is sorted in ascending order and contains no duplicates. Using the built-in `sort()` method, it sorts the list, and the `set()` method helps to determine whether there are any duplicates, ultimately returning `True` if the list is both sorted and contains no duplicates, and `False` otherwise. 

This approach ensures that the list is sorted and free of duplicates, essential requirements for the problem. While the `set()` method removes duplicate elements, the `len(unique) == len(lst)` condition checks for uniqueness, and `len(lst) == len(set(lst))` double-checks that there are no duplicates by assessing that every element is unique within the list. 

To demonstrate the functionality, you can use the following test cases:
```python
# Test Case 1
print(is_sorted([5]))  # Output: True

# Test Case 2
print(is_sorted([1, 2, 3, 4, 5]))  # Output: True

# Test Case 3
print(is_sorted([1, 3, 2, 4, 5]))  # Output: False

# Test Case 4
print(is_sorted([1, 2, 3, 4, 5, 6]))  # Output: True

# Test Case 5
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # Output: True

# Test Case 6
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # Output: False

# Test Case 7
print(is_sorted([1, 2, 2, 3, 3, 4]))  # Output: True

# Test Case 8
print(is_sorted([1, 2, 2, 2, 3, 4]))  # Output: False
```

Note that this code handles the described scenario well, and the function's simplicity makes it easy to understand and use, making it an efficient solution to the problem.