```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with sample inputs
test_get_positive = []
test_get_positive.py  #[-1, 2, -4, 5, 6]
test_get_positive.py  += [[5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]]

print("Test Results:")
for test in test_get_positive:
    print(f"Input: {test}, Should be Positive: {get_positive(test)}")
```