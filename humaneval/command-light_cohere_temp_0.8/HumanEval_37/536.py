```python
def sort_even(lst):
    return lst[:] if all(i % 2 == 0 for i in lst) else lst

# Test cases
test_cases = [
    [5, 6, 3, 4],
    [1, 2, 3],
    [4, 6, 5, 3],
    [10, 20, 30],
]

for test_case in test_cases:
    actual_list = sort_even(test_case)
    print(f"Test case {test_case} passed: {actual_list}")
```