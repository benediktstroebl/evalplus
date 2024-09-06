```python
def sort_third(lst):
    """Sorts a list l such that all numbers not divisible by three are at the beginning"""
    return lst[:[lambda lst: lst.is_odd(int) for int in lst if int % 3 != 0] + lst[::3]

# Test cases
test_sort_third = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [1, 5, 6, 3, 4, 8, 9],
]

for case in test_sort_third:
    assert sort_third(case) == case
```