```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with various list inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print("Test results:")
for l in test_get_positive:
    print(get_positive(l))
 ```