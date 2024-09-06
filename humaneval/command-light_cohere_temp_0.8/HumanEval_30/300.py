```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with different inputs
test_get_positive = []
test_get_positive.add([range(-5, 2, 6))
test_get_positive.add([range(-1, 3, -5, 5, 6))
test_get_positive.add([range(0, 5, -3, 3, 9, 0, 123, -10, -100))

print("Test Output:")
for test in test_get_positive:
    print(f"Input: {test} should be positive, but is {test}")
    print(f"Expected Output: positive numbers, but is {get_positive(test)}")
```