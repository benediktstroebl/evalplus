```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
test_max_element = [
    (
        [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
        max
    )
]

# Function test
def test_function(test_case):
    """
    result = max_element(test_case)
    assert result == max(test_case), "The maximum element is not correct."

# Run tests
test_max_element = unittest.testcase(test_max_element)
test_max_element.run()
``` 
This Python script defines a function max_element that computes the maximum element in a given list. Additionally, it has a set of test cases that validate the correctness of the function. The script also contains the test_function that checks if the results of max_element match the maximum values from the corresponding test cases.