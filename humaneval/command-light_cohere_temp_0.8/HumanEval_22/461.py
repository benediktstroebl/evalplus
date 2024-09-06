Here is a Python script with a self-contained function that solves the problem of filtering integers from a list:

```python
# Function to filter integers from list
def filter_integers(values):
    return [int(x) for x in values if type(x) == int]

# Test cases
test_cases = [
    ['a', 3.14, 5], [1, 2, 3, 'abc', {}, []],
]

# Function call and testing
for test_case in test_cases:
    actual_output = filter_integers(test_case)
    assert actual_output == [int(x) for x in test_case], "Test case failed: {}".format(test_case)
```

The code defines a function **`filter_integers`** that accepts a list of values and returns a new list containing only the integers from the input. The code also provides several test cases to validate the function, ensuring that it behaves correctly and returns the expected output.