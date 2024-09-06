```python
def sort_even(lst):
    return lst[:] if all(n % 2 == 0 for n in lst) else lst[:0] + [n for n in lst if n % 2 != 0]

# Test cases
test_sort_even = []
test_sort_even.append([5, 2, 3])
test_sort_even.append([5, 6, 3, 4])
test_sort_even.append([5, 1, 4, 6])

# Function call and result
print(sort_even(test_sort_even))
```