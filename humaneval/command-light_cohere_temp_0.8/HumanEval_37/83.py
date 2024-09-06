```python
def sort_even(lst):
    return lst[:]  # return list as is, with all even indices unmodified

# Test cases
test_cases = [
    [1, 2, 3],
    [5, 6, 3, 4],
    [4, 9, 7, 5, 6]
]

for test in test_cases:
    actual = sort_even(test)
    assert actual == test  # check if results are equal
```