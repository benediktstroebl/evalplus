```python
def sort_third(lst):
    # Sort the list so values divisible by 3 are together and others are not
    return sorted(lst, key=lambda x: (3 * x) // 3, x)

# Test
test_list = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(test_list))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
```