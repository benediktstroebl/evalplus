```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
tests = {
    "Test 1":
    input = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(input) == 123
}

#Main function test
def test_max_element():
    assert max_element(tests["Test 1"]) == 123
``` 
This script defines a Python function `max_element` that takes a single argument `l`, which is expected to be a list. Then, it uses the max function to find the maximum element in the list. After, the function is passed through several test cases. 

The test cases use the list `tests` to define the input data and expected output for each test, and the `test_max_element` function is used to run the tests.