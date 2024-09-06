Here is a self-contained Python function that solves the problem of generating a string of numbers from 0 up to n:
```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive."""
    return f"0 {n} {" + str(n) + "} "

# Test cases
test_str = string_sequence(0)
assert test_str == '0'
test_str = string_sequence(5)
assert test_str == '0 1 2 3 4 5'
```
This function takes an integer n as input and returns a string containing space-separated numbers from 0 up to and including n. It uses string formatting to create the desired output format. The test cases ensure that the function is correctly implementing the desired behavior.