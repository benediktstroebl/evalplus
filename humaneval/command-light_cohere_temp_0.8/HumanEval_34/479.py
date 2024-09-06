```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float()]

# Test cases
test_cases = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [5, 3, 7, 2, 'three', 0, 3, "123"],
    [1, 'a', 2, 3, 'abc', 4],
    [5, 'five', 'five', '5'],
    [()],
    [[]]
]

for case in test_cases:
    print(unique(case))
```