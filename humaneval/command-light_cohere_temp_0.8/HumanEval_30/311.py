```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with different inputs
test_positive = get_positive([-1, 2, -4, 5, 6])
test_positive_negative = get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Print the results
print("Positive numbers:", test_positive)
print("Negative numbers:", test_positive_negative)
```