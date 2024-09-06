```python
def pairs_sum_to_zero(l):
    if sum(l) == 0:
        return True
    else:
        return False

# Tests
test_pairs_sum_to_zero = [
    ([1, 3], False),
    ([1, 2, 3], False),
    ([2, 4, -5], True),
    ([1], False),
    ]

test_pairs_sum_to_zero

for test_case in test_pairs_sum_to_zero:
    print(f"{test_case[0]} + {test_case[1]} = {test_case[2]}...")
    result = pairs_sum_to_zero(test_case)
    assert result == test_case[2], f"Expected {test_case[2]}, but got {result}"
```

This code defines a function `pairs_sum_to_zero` that checks if two elements in an input list sum to zero. The test cases are defined in the `test_pairs_sum_to_zero` list, and each test case consists of a pair of integers and the expected result. The function is then passed through to the test cases, and the output is compared against the expected result. The output will be an assertion error if the function returns the wrong value for a given test case.