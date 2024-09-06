```python
def pairs_sum_to_zero(l):
    return sum(x + y for x, y in zip(l, l[1:])) == 0

# Example usage
test_cases = [
    [],    # [1]
    [1, 3], # [1, 3]
    [-2, 1], # [1, -2]
    [2, 4, 7], # [2, 4, 7]
    [1]        # [1]
]

for case in test_cases:
    result = pairs_sum_to_zero(case)
    print(result)
```
This function performs the summation of pairs in a list and checks if it equals zero. It uses the process to find two elements that add up to zero. The final output will be True if this condition is met, and False otherwise.