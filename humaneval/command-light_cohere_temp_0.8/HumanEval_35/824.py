```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test cases
test_max_element = [
    ( [], float('-inf') ),
    ( [1, 2, 3], 3),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 123),
    ( [1, 2, 3, 4, 5], 5),
    ( [ -5, -3, 3, -10, -8, -7 ], -10),
    ( [123, 2, 1], 2),
    ( [1, 2, 3, 4, 5, 6, 7, 8, 9 ], 9)
]

# Function to test the max_element function
def test_max_element_function(test_cases):
    for item in test_cases:
        assert max_element(item) == float(item[1])
```