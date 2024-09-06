```python
def sort_even(lst):
    return lst[:] if len(lst) % 2 == 0 else lst[:len // 2] + [lst[-len // 2 :]]

# Test cases
test_sort_even = []
test_sort_even.push_list([1, 2, 3])
test_sort_even.push_list([5, 6, 3, 4])
test_sort_even.push_list([10, 20, 30, 80])

for test in test_sort_even:
    actual = sort_even(test)
    assert actual == [3, 6, 5, 4], f"Test case {test} failed: {actual}"
```