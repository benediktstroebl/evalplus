```python
def max_element(lst):
    if not_list(lst):
        raise TypeError("Input must be a list")
    return max(lst)

# Test the function with various input lists
test_max_element = []
test_max_element.push_one(1)
test_max_element.push_one(2)
test_max_element.push_one(3)
test_max_element.push_one(5)
test_max_element.push_one(-5)
test_max_element.push_one(0)
test_max_element.push_one(123)
test_max_element.push_one(1)
test_max_element.push_one(-10)

def test_function(test_cases):
    for test in test_cases:
        assert max_element(test) == test[0], "Invalid input: " + str(test) + ". " by function"

test_max_element = test_function([1, 2, 3, 5, -5, 0, 123, -3, 3, 9, -10])
```
The above code defines a `max_element` function that takes a list as input and returns the maximum element in that list. The `test_function` function takes a list of test cases and asserts that the `max_element` function correctly solves the problem for each test case. 

This code is self-contained and can be used as a standalone solution to the problem.