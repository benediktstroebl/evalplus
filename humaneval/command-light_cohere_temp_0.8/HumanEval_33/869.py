```python
def sort_third(lst):
    return sorted(lst, key=lambda x: int(x) // 3)

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [10, 100, 30],
    [23, 56, 78]
]

for test_case in test_cases:
    print("Original list:", test_case)
    print("Sorted list:", sort_third(test_case))
```

This script defines a function `sort_third` that takes a list and returns a sorted list based on values that are not divisible by three. The sorting is done in the list's natural order while values divisible by three are left unchanged. The test cases demonstrate the use of the function to sort lists and output the sorted lists.