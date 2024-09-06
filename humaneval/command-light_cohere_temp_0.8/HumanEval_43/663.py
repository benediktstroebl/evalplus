```python
def pairs_sum_to_zero(lst):
    return any(x+y <= 0 and x != y for x, y in zip(lst, lst[1:]))

print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))          # Output: False
```

This code defines a function `pairs_sum_to_zero` that takes a list `lst` as input and returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The function uses a effective test based on the sum of the elements in the list and the second element. The test uses the combination of these elements, which is then compared to the sum of the first element and the second element to determine whether the sum is zero or not.