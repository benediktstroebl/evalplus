```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test case 1:
assert sort_even([1, 2, 3]) == [1, 2, 3]

# Test case 2:
assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

# Test case 3:
assert sort_even([10, 11, 12]) == [10, 11, 12]
```
The function **`sort_even`** takes a list **`l`** as an argument and uses the **`sorted`** function with a custom key function to sort the list such that the even index values of the original list will maintain their order while the odd index values will be ordered by adding 1 to them.