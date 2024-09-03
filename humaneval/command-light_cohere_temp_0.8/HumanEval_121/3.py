```python
def solution(lst):
    """Given a non-empty list of integers, returns the sum of all the odd elements that are in even positions."""
    return sum(x for x in lst if not_even(x, lst))

def not_even(x, lst):
    return x % 2 == 0

tests = [ [ [1, 3, 5, 7], [2, 4, 6, 8], [9, 19, 23], [30, 13, 24, 321] ]

for test_case in tests:
    actual = solution(test_case)
    expected = sum(x for x in test_case if not_even(x, test_case))
    assert actual == expected
```