```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function with a list of lists
test_list = [
    [1, 2, 3],
    [5, 3, 5],
    [2, 3, 5]
]

result = incr_list(test_list)
print("Test 1 result:", result)

# Test the function with a list of numbers
test_num = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_num)
print("Test 2 result:", result)
```
This script defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements incremented by 1. The test cases use two types of lists: one with sublists and another with numbers, and the function is tested with them to ensure it works correctly.