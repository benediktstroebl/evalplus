```python
def sort_third(lst):
    """Sorts a list l such that values at indices divisible by three are moved to the front, and the rest are moved to the back."""
    lst[:::3] = lst[::3] + lst[1::3]
    return lst

# Test cases for the function
print("Test Case 1:", sort_third([1, 2, 3]))  # Expected output: [1, 2, 3]
print("Test Case 2:", sort_third([5, 6, 3, 4, 8, 9, 2])) # Expected output: [2, 6, 3, 4, 8, 9, 5]
print("Test Case 3:", sort_third([10, 11, 12, 13, 14, 15, 16]))  # Expected output: [10, 11, 12, 13, 14, 15, 16]
```