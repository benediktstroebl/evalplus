```python
def sort_even(lst):
    return lst[:][:]: # slice to exclude odd indices

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [0, 7, 5, 6]
]

for case in test_cases:
    actual = sort_even(case)
    expected = case
    print(f"Test case {case}:\n{actual} != {expected}")
```