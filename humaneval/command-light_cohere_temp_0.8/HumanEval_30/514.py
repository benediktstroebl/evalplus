```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a list containing both positive and negative numbers
test_get_positive = []
test_get_positive.push_(-1)
test_get_positive.push_(2)
test_get_positive.push_(-4)
test_get_positive.push_(5)
test_get_positive.push_(6)

print(get_positive(test_get_positive))  # Expected output: [2, 3, 5, 6]
```