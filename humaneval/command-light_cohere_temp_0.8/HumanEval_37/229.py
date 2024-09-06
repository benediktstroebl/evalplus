```python
def sort_even(lst):
    return sorted(lst, key=lambda x: x if x % 2 else x + 1)

# Test cases
tests = {
    "Input: [1, 2, 3, 4, 5, 6]
    "Expected Output: [1, 2, 3, 4, 5, 6]"
}

def test_function(test_case):
    actual_output = sort_even(test_case["Input"])
    assert actual_output == test_case["Expected Output"]

# Run the tests
test_function(tests)
```

The script defines a function `sort_even` that sorts a list using a key function that determines the order based on whether the number is even or odd. The test cases are defined to verify the behavior of the function, passing the input list and expected output. The test function uses the dry running assertion (assert) to check if the actual output matches the expected output.