```python
def sort_third(lst):
    """Sorts a list l such that elements not divisible by three are at the beginning"""
    return sorted(lst, key=lambda x: (x // 3) % 2)

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [5, 9, 6, 2, 8, 3, 4]
]

for case in test_cases:
    print(sort_third(case))  # Should print [2,3,4,5,6,8,9]
```