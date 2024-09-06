```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test the function with some examples
test_get_positive = []
test_get_positive.add([range(-5, -1, 6))
test_get_positive.add([range(5, 3, -1))
test_get_positive.add([range(0, 123, 10))
test_get_positive.add([range(10, 2, -3))

print("Test Results:")
for test in test_get_positive:
    print(f"Input: {test}, Expected Output: {get_positive(test)}")
```