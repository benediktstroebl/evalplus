```python
def pairs_sum_to_zero(l):
    return any(sum(x) == 0 for x in l) and any(x != 0 for x in l)

# Test the function with various input lists
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))          # Output: False
```