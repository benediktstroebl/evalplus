```python
def sort_third(l: list):
    """Sorts list l such that values not divisible by three are in front, and are sorted.
    """return sorted(l)[::-1] if len(l) > 2 else l

# Example test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4, 8, 9, 2],
    [5, 6, 3, 4, 8, 9, 5, 2]
]

for i, tc in enumerate(test_cases):
    actual = sort_third(tc)
    assert actual == tc
```