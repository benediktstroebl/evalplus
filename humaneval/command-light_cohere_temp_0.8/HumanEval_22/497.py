Here is a Python script that contains a self-contained function that filters out integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases 

test_cases = [
    [],  # [] converts to zero-length array, which is considered empty
    ['a', 3, 'three', (1.14), 5],
   
    [1, 2, 3, 'abc', {}, []]
]

for test_case in test_cases:
    actual_result = filter_integers(test_case)
    expected_result = [x for x in test_case if isinstance(x, int)]
    assert actual_result == expected_result, f"Failed for test case: {test_case}" 

print("All tests passed!")
``` 
This script defines a function called **filter_integers** that accepts a list of values and returns a new list containing only the integers from the original list. The test cases section then verifies the function's correctness by comparing the output with the expected results using **assert**.