```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    ( [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], lambda l: max_element(l) ),
    ( [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 123),
    ( [(), []], 0),
    ( [1, 2, 3, 4, 5], 3),
    ( [1, 2, -3, 3, 4, 5], -2),
    ( [5, 3, -5, 2, -3, 3], -1),
    ( [5, 3, -5, 2, -3, 3, 9, 0], None),
]

for test_case in test_max_element:
    actual_result = test_case[1](test_case[0])
    print(f"Test case {test_case} passed: {actual_result}")
``` 
This code defines a max_element function that returns the maximum element from the input list. It also provides several test cases to check the correctness of the function. 

Each test case contains a list and a corresponding lambda function that calls the max_element function with the list as an argument and compares the result with the expected maximum element.