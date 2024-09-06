```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
test_get_positive = [
    dict(
        [input=" [-1, 2, -4, 5, 6] ],
        [2, 5, 6],
    ),
    dict(
        [input=" [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]"],
        [5, 3, 2, 3, 9, 123, 1],
    ),
]

for case in test_get_positive:
    assert get_positive(case['input']) == case['expected'])
```