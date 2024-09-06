```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    ( [], 3 ),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 2 ),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 10 ),
    ( [1, 2, 3, 4, 5, 6], 0 ),
    ( [12, 34, 12], blank_test ),
]

def blank_test():
    pass

def test_max_element():
    for test_case in test_max_element:
        assert max_element(test_case[0]) == test_case[1]

# Main program
if __name__ == "__main__":
    print("Running tests:")
    test_max_element()
    print("All tests passed!")
```
The code defines a function max_element that calculates the maximum element in a list, and then provides several test cases to ensure its correctness. The code uses the example lists and asserts that the max_element function returns the correct result for each case. The main program executes the will print the test status.