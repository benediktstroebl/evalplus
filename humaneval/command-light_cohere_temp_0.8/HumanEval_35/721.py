```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
tests = [
    {
        "Input": [1, 2, 3], 
        "Expected Output": 3
    },
    {
        "Input": [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
        "Expected Output": 123
    },
    # Add more test cases as needed
]

for test in tests:
    assert max_element(test["Input"]) == test["Expected Output"] 
``` 
This Python function uses the `max()` built-in function to return the maximum element in the list. 
The test cases ensure the right behavior of the function.