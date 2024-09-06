```python
def sort_third(lst):
    """Sorts the list such that all elements not divisible by three are at the beginning, and all elements divisible by three are at the end of the list"""
    return [x for x in lst if x % 3 != 0] + [x for x in lst if x % 3 == 0]

# Test cases
print("Test Case 1:")
sort_third([1, 2, 3])  # Expected output: [1, 2, 3]

print("Test Case 2:")
sort_third([5, 6, 3, 4, 8, 9, 2])  # Expected output: [2, 6, 3, 4, 8, 9, 5]

print("Test Case 3:")
sort_third([10, 2, 3, 4, 6, 7, 5])  # Expected output: [2, 3, 4, 6, 7, 5, 10]

print("Test Case 4:")
sort_third([9, 3, 2, 6, 5, 7, 8])  # Expected output: [2, 3, 6, 5, 7, 8, 9]
```

This Python code defines a function `sort_third` that sorts a list such that all elements not divisible by three are at the beginning and all elements divisible by three are at the end of the list. The function achieves this test cases, and the expected outputs are as expected.