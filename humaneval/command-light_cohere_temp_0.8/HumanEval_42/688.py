```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    return result

# Test cases
test_incr_list = [
    (=[1, 2, 3], [2, 3, 4]),
    ( [5, 3, 5, 2, 3, 3, 9, 0, 123 ], [6, 4, 6, 3, 4, 4])
]

# Function call and result comparison
test_incr_list_result = incr_list(test_incr_list)
for case, expected_result in zip(test_incr_list, test_incr_list_result):
    print(f"Test case {case}: Expected {expected_result}, got {case}")
```  This Python code defines a function called `incr_list` that takes a list as input and returns a new list with elements incremented by 1. The function uses list comprehension to create the new list. The test cases define two lists of input lists and corresponding expected results for the `incr_list` function. The code then calls the `incr_list` with each test case and compares the result against the expected result using a loop. 

This code follows the PEP 8 style and is a self-contained solution to the problem of incrementing a list of integers.