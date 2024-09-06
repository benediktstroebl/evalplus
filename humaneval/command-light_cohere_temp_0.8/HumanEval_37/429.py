```python
def sort_even(l: list):
    return l[::2:]

# Test the function
test_even = [5, 6, 3, 4]
res = sort_even(test_even)
assert res == [3, 6, 5, 4]

# Test the function with an empty list
test_empty = []
res = sort_even(test_empty)
assert res == []

# Test the function with a list of numbers
test_numbers = [1, 2, 3, 4, 5, 6]
res = sort_even(test_numbers)
assert res == [3, 6, 5, 4]
```

The function `sort_even` takes a list `l` as an argument and returns a list `l'` such that the elements at even indices are sorted in the same order as in `l`. The returned list is then returned.