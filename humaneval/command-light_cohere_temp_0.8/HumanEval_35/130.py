```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test cases
test_max_element = {
    "test basic": lambda: max_element([1, 2, 3]) == 3,
    "test empty list": lambda: max_element([]) == 0,
    "test negative numbers": lambda: max_element([5, -5, 2, -3, 3, -10]) == -10,
    "test large numbers": lambda: max_element([123, 124, 125]) == 125,
    "test mixed numbers": lambda: max_element([0, 9, 2, 123, -10, 5]) == 123
}

# Run the tests
for test in test_max_element.all print("Running {}")
``` 
This code defines a max_element function that computes and returns the maximum element in a given list. It also includes a set of test cases that check the correctness of the max_element function for different scenarios. 

The code then executes each test case and displays the result.