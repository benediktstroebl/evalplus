```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function
test_get_positive = []
test_get_positive.push_back(get_positive([-1, 2, -4, 5, 6]))
test_get_positive.push_back(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
test_get_positive.push_back(get_positive([5, 0, -5, 2, -3, 3, 9, -1, 7, 8]))
test_get_positive.push_back(get_positive([1, 2, 3, -4, -5]))

print("Positive numbers:", end="eraspace"))
for test in test_get_positive:
    print(test, end=" ")
```