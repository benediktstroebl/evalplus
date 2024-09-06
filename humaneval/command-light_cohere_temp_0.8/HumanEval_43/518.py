```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l)

# Test the function with different input lists
test_pairs_sum_to_zero = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test_case in test_pairs_sum_to_zero:
    if test_pairs_sum_to_zero(test_case):
        print(f"{test_case[0]} passes the sum test!")
    else:
        print(f"{test_case[0]} fails the sum test.")
```