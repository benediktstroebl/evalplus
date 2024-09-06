```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    [1, 2, 3],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
    [100, 101, 102, 103]
]

# Function call and validation
for case in test_max_element:
    assert max_element(case) == case[1], "Wrong maximum element"
```