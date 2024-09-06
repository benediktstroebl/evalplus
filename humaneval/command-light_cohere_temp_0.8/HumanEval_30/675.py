```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
tests = [
    ([-1, 2, -4], [2, 5, 6]),
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], [5, 3, 2, 3, 9, 123]))
] = get_positive(tests)

print("Test cases passed:", end())
```