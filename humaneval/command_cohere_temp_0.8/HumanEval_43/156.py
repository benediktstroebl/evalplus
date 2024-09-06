```python
def pairs_sum_to_zero(l):
    # iterate through all pairs
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False
```

This function uses two nested loops to iterate through all possible pairs of elements in the input list `l`. It determines if the sum of the pairs is equal to zero. If any pair sums to zero, it returns `True`. If no pairs sum to zero, it returns `False`. This approach provides a concise solution to the problem, as it directly addresses the requirement of finding two distinct elements that sum to zero.

Here's how you can use this function and test it with the provided cases:
```python
# Test the function with the provided cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))  # Output: False
```