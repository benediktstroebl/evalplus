```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 == 0 else x+1)

# Test case 1
print("Test case 1:")
print(sort_even([1, 2, 3]))
# Expected output: [1, 2, 3]

# Test case 2
print("Test case 2:")
print(sort_even([5, 6, 3, 4]))
# Expected output: [3, 6, 5, 4]

# Test case 3
print("Test case 3:")
print(sort_even([10, 20, 30, 40]))
# Expected output: [10, 20, 30, 40]
```
This script defines a function `sort_even` that sorts a list according to the odd indices of the elements. It uses a `key=lambda x: x if x % 2 == 0 else x+1` as the sorting key to ensure the even elements are sorted as they appear.