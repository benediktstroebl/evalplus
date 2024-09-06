```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
test_max_element = [
    ( [], float('-inf') ),
    ([ 1, 2, 3 ], 2),
    ([ 5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10 ], 123),
    ([ -5, -3, 3, 9, 0 ], -3),
    ([-5,-10, -20,-30, -100 ], -100)
]

def test_function(test_case):
    actual = max_element(test_case)
    expected = test_case[1]
    assert actual == expected, f"Failed test case: {test_case}"

test_max_element()
``` 
This Python code defines a function max_element that calculates and returns the maximum element from a list using the built-in function max. The code also provides a list of test cases, each containing a list of numbers and the expected maximum. The test_max_element function uses the max_element function to get the actual maximum element and compares it with the expected maximum element. The code then checks if the test case passed, if not, it raises an AssertionError with a detailed error message.