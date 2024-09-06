```python
def sort_even(lst):
    return lst[:][:::len(lst)//2::2]

# Test cases
test_sort_even = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [0, 10, 1, 9]
]

for test in test_sort_even:
    actual = sort_even(test)
    assert actual == test
```