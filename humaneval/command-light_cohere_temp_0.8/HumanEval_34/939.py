```python
def unique(l: list):
    return list(set(l))

# Test cases
tests = [
    [
        [5, 3, 5, 2, 3, 3, 9, 0, 123],
    ],
    ['string', 'hello world'],
    [range(1000, 0, -1)],
    [set([1, 2, 3])],
]

for test in tests:
    actual = unique(test)
    print(f"Test case {test}: {actual}")
    assert actual == [x for x in test if x not in [5, 3]]
```