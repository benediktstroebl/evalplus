```python
def sort_even(lst):
    return lst[:] if all(x % 2 == 0 for x in lst) else lst

#Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [100, 20, 80],
]

for case in test_cases:
    assert sort_even(case) == case
```