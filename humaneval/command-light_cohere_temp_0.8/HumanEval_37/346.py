```python
def sort_even(lst):
    return lst[:] if len(lst) % 2 == 0 else lst[:len // 2] + lst[len // 2:]

# Test the function
# Check the correctness of the function using a basic set of test cases
assert(sort_even([1, 2, 3]) == [1, 2, 3])
assert(sort_even([5, 6, 3, 4]) == [3, 6, 5, 4])
```