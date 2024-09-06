```python
def pairs_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l)

# Example usage:
test_cases = [
    [1, 3, 5, 0],
    [1, 3, -2, 1],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test_case in test_cases:
    result = pairs_sum_to_zero(test_case)
    print(f"Test case {test_case} --> {result}")
```
The function checks if there are two distinct elements in the list that sum to zero, and returns `True` if they do, and `False` otherwise. The function is self-contained and requires no external variables.