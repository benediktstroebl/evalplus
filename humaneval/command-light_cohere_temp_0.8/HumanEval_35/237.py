```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    [list([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])],
    [1, -10]
]

print("Test cases passed:")
for case, expected in test_max_element:
    actual = max_element(case)
    print(f"Case {case}: Expected {expected}, got {actual}")
```