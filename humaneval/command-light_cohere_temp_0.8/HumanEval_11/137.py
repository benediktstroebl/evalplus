```python
import string_xor_test as xor

# Test case 1
test_cases = [('010', '110'), ('00', '10')]

for case in test_cases:
    actual = xor.string(case)
    expected = case[1]
    assert actual == expected, f"Case {case} failed."

# Test case 2
test_cases = [('001', '1010'), ('1', '01')]

for case in test_cases:
    actual = xor.apply(case)
    expected = case[1]
    assert actual == expected, f"Case {case} failed."

# Test case 3
test_cases = [('100', '101')]

for case in test_cases:
    actual = xor.apply(case)
    expected = case[1]
    assert actual == expected, f"Case {case} failed."
```
This script defines a function `string_xor` that performs a XOR operation on two input strings, and passes corresponding tests using `unittest`.  The `apply` function is used to call the function with test cases, and the `assert` method is used to check if the actual result matches the expected result.