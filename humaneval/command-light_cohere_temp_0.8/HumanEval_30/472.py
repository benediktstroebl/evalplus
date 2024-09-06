```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with some examples
test_get_positive = []
test_get_positive.add([range(1, 6))
test_get_positive.add([range(-1, -6))
test_get_positive.add([range(0, 1)])
test_get_positive.add([range(-3, -3)])
test_get_positive.add([range(123, 1)])
test_get_positive.add([range(10, -1)])

print(f"Test results: {")
for test in test_get_positive:
    print(f"Input: {test} - Expected: [{])
    print(f"      {test[0]}")
    print(f"      {test[-1]}")
    print()")

print(f"------------------------------")
```
Do you want to find the correct output or solutions?  The output will be a list of expected results, depending on the provided inputs.