```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
test_cases = [{'list([1, 2, 3])} ]

def test(test_case):
    test_list = [x + 1 for x in test_case]
    return test_list == test_case

# Run all tests and print results
for test_case in test_cases:
    test_res = test(test_case)
    print(f"Testcase {test_case} passed: {test_res}")
```

This script defines a function `incr_list` that returns a new list with elements incremented by 1. It also defines a test case 1 with a list of lists, and a function `test` that checks if a given list of lists passes a specific test. The script then runs all tests and prints the results.