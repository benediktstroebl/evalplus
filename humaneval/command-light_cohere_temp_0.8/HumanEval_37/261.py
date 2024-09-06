```python
def sort_even(lst):
    return lst[:] + [lst[i] for i in range(1, len(lst))] + lst[-1:]

# Test cases 1
print("Test case 1:", end="")
print(sort_even([1, 2, 3]))
print("------")

# Test cases 2
print("Test case 2: ", end="")
print(sort_even([5, 6, 3, 4]))
print("------")

# Test cases 3
print("Test case 3: ", end=")
print(sort_even([2, 6, 3, 5]))
print("------")

# Test cases 4
print("Test case 4: ", end="")
print(sort_even([2, 4, 8, 6]))
print("------")

# Test cases 5
print("Test case 5: ", end=")
print(sort_even([10, 20, 30]))
print("------")
```

This script defines a function `sort_even` that sorts a list in even values in ascending order. It uses the method of creating new list elements by combining the original list with the even index values of the original list.