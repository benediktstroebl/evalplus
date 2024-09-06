```python
def pairs_sum_to_zero(l):
    return any(x + y <= 0 for x, y in zip(l, l[1:]))

# Test the function
test_passes = True
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for case in test_cases:
    if not_passes = not(pairs_sum_to_zero(case)):
        test_passes = False

if test_passes:
    print("All tests passed!")
else:
    print("Tests failed.")
```