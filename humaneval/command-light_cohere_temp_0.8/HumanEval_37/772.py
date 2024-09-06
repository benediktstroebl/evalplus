```python
def sort_even(lst):
    return lst[:][:math.isprime(i) for i in range(2, len(lst))]]

# Test cases
tests = [
    [list({i for i in range(1, 7)})]  # True
    , [2, 3, 5, 6]  # True
    , [5, 6, 3, 4]  # True
    , [1, 20, 51]  # False
    , [10, 2, 3]  # False
]

for test_case in tests:
    assert sort_even(test_case) == test_case
```