```python
def sort_even(lst):
    return lst[:] if len(lst) % 2 == 0 else lst[:::2] + [lst[-2::2]] + lst[::2:]

# Test
test_sort_even = [1, 2, 3]
test_sort_even == [1, 2, 3]
test_sort_even[::-1] == [3, 2, 1]

# The output should be correct, use the above test cases to verify the correctness of your function.
```