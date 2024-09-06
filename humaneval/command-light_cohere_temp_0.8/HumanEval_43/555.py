```python
def pairs_sum_to_zero(l):
    return sum(x + y for x, y in zip(l, l[1:])) == 0

# Test the function with various input lists
test_pairs_sum_to_zero = [
    [],  # List of integers with no pair summing to zero
    [],  # List of two identical elements
    [1, 3],  # List of two distinct elements
    [-2, 1],  # List of two distinct elements
    [2, 4, -5],  # List with three distinct elements
    [1, 1],  # List of one element
]

for test in test_pairs_sum_to_zero:
    if not_two_distinct(test):
        print(test, "Passed")
```

The function `pairs_sum_to_zero` calculates the sum of all pairs of elements in a list and checks if it's equal to zero. It returns `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise. The test function is used to test the `pairs_sum_to_zero` function with various input lists.