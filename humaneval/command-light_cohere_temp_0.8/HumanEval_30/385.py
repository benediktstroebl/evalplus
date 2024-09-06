```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num > 0]

# Test the function with different inputs
test_get_positive = []
test_get_positive.append([5, [1, 2, 3, -4, 5, 6])
test_get_positive.append([2, [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
test_get_positive.append([-1, -])
test_get_positive.insert([0])

print("The list of positive numbers is:")
print(test_get_positive)
```