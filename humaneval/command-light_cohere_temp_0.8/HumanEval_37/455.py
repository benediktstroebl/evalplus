```python
def sort_even(lst):
    return lst[:] + [x for x in lst[1::2] if x % 2 == 0] + lst[-1:]

# Test cases
test_sort_even = []
test_sort_even.add([1, 2, 3])
test_sort_even.add([5, 6, 3, 4])
test_sort_even.add([5, 1, 2, 3])
test_sort_even.add([5, 6, 5, 4])
test_sort_even.add([5, 3, 1, 2])
test_sort_even.add([5, 6, 4, 5)

# Function call
sort_even(test_sort_even)
```