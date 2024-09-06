```python
def get_positive(input_list):
    """Return only positive numbers in the list"""
    return [num for num in input_list if num >= 0]

# Unit tests
test_get_positive = False
def test_function():
    assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

def test_other_function():
    assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

# Main function to execute the tests
def execute_tests():
    global test_get_positive, test_other_function
    test_get_positive = True
    test_other_function()

if __name__ == "__main__":
    execute_tests()
```

The code defines a function called `get_positive` that takes a list as input and returns a new list with only the positive numbers from the input. It then contains a test functions, which contain assertions that check the correctness of the `get_positive` function with different input scenarios. Finally, the code executes the main function with the `if __name__ == "__main__"` guard, which starts the execution of the test suite.