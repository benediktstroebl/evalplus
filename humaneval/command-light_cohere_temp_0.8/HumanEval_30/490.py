```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with various inputs
test_get_positive = []
test_get_positive.push([-1, 2, -4, 5, 6])
test_get_positive.push([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

print(f"Function Output: {test_get_positive}")

for idx, val in enumerate(test_get_positive):
    if not in get_positive(test_get_positive):
        print(f"Error: Negative number {val} found but expected positive", idx)
```