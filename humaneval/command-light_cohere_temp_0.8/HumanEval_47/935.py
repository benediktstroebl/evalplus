```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
test_median = [
    [
        [],
        [10, 20, 30],
        [100, 200, 300],
        [-100, 40, 200, 300],
        [-10, 4, 6, 1000, 10, 20]
    ]
)

for t in test_median:
    actual = median(t)
    expected = t[1]  # due to alternating order of odd and even elements
    assert actual == expected
```