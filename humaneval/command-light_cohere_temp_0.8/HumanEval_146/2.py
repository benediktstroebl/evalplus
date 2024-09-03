```python
def specialFilter(nums):
    return sum([isdigit(x) == True and x >= 10 and x % 10 != -5 and str(x)[1] == str(x)[-] for x in nums])

# Test cases
test_cases = [
    [15, -73, 14, -15,],
    [33, -2, -3, 45, 21, 109,],
    [123, 45, 56, 67, 98, 7, -88,],
    [2134, -6567, 9868, -109]
]

for t in test_cases:
    actual = specialFilter(t)
    expected = len(t)
    assert actual == expected
```