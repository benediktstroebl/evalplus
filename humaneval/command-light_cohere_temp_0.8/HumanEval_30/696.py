```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with different list inputs
# Test with list containing only positive numbers
test_positive = [1, 2, 3, 4, 5]
get_positive(test_positive)
# Test with list containing negative numbers
test_negative = [-1, 2, -4, 5, 6]
get_positive(test_negative)
# Test with mixed positive and negative numbers
test_mixed = [5, 3, -5, 2, -3, 3, 9, 0, 123, -10]
get_positive(test_mixed)
```