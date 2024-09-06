Here is a self-contained Python script that defines and implements a function to generate a string of numbers from 0 to n:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n + 1) + "0 }"

# Test cases
test_string_sequence = [
    deftest(string_sequence(0))
    assert '0' == test_string_sequence, "Should start with 0"
   
    deftest(string_sequence(1))
    assert '0 1' == test_string_sequence, "Should start with 0 and increment"
    deftest(string_sequence(5))
    assert '0 1 2 3 4 5' == test_string_sequence, "Should contain all numbers till n"
    deftest(string_sequence(-1))
    assert '0 ' == test_string_sequence, "Should start with 0"
    deftest(string_sequence(0))
    assert '0' == test_string_sequence, "Should start with 0"
]
test_string_sequence()
```
This code defines a `string_sequence` function that returns a string containing space-delimited numbers from 0 to n. It then provides several test cases to verify the function's behavior.

The `deftest` helper function is used to create test cases, which assert the expected and actual values of the `string_sequence` function.