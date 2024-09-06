Here is a self-contained Python function that filters out integers from a list of mixed values:
```python
def filter_integers(values):
    return [element for element in values if isinstance(element, int)]

# Test cases
test_cases = [
    [],  # [] content
    ['a', 3, 'hello'],  # String and non-int mixed input
    [1, 2, 'three'],   # Ints mixed with str and other non-int elements
    ]

for test_case in test_cases:
    actual_output = filter_integers(test_case)
    assert actual_output == [int(x) for x in test_case], f"Test case {test_case} failed"
```
This code defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input. It tests the using a set of test cases that cover various scenarios, including empty lists, strings, non-integer values, and lists of integers. The code then uses the validation to ensure that the output of the `filter_integers` function matches the expected output for each test case.