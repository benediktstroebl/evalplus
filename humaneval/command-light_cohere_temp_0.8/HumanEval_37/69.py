```python
def sort_even(lst):
    """Sorts the list l such that all even indices are equal."""
    return sorted(lst, key=lambda x: x % 2 == 0)

# Test cases
test_sort_even = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [2, 8, 10, 4],
]

# Function call and check
for test in test_sort_even:
    assert sort_even(test) == test
```