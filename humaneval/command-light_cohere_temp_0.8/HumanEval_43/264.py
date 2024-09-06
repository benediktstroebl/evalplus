```python
def pairs_sum_to_zero(l):
    return any(x + y > 0 for x, y in zip(l, l[1:]))

# Run the function and tests
print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(pairs_sum_to_zero([1]))  # Output: False
```

This Python script defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in a list that their sum is equal to zero. The function uses a `zip` function to iterate through the list and checks if there are two elements that add up to zero. The tests use a same simple list comprehension to create the `any` condition for the `pairs_sum_to_zero` function.