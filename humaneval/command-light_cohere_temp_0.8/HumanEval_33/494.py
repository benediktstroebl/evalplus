```python
def sort_third(lst):
    """Sorts list l such that values divisible by 3 appear first"""
    return sorted(lst, key=lambda x: int(x) // 3 if x % 3 == 0 else x)

# Test cases
print("First Test:", sort_third([1,2,3]))  # Expected output: [1, 2, 3]
print("Second Test:", sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
print("Third Test:", sort_third([10, 2, 3, 20, 30, 40]))  # Expected output: [10, 2, 30, 3, 20, 40]
```