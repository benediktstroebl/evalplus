```python
def max_element(lst):
    return max(lst)

# Test cases
test_max_element = [
    ( [], 5 ),
    ( [ 1, 2, 3], 3 ),
    ( [ 5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10 ], 123 ),
    ( [ -5, -3, -10, -8, -7 ], -8 ),
    ( [ 5, -5, 3, -3, 12, 9, 0 ], 5 ),
    ( [ '', 'Hello', 'world!' ], 55 )
]

# Function to test the max_element function
def test_function(test_case):
    assert max_element(test_case) == test_case[1], "Function didn't return expected result"

# Run the test suite
test_function(test_max_element)
```