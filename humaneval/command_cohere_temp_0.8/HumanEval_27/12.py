```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.islower() else c.upper() for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string with flipped case, as described in the prompt.

To test this function, you can call it with different inputs and compare the output with the expected results. Here's an example:
```python
# Test case with lowercase input
input_str = 'hello world'
expected_output = 'hELLO WORLD'
output = flip_case(input_str)
assert output == expected_output

# Test case with uppercase input
input_str = 'HELLO WORLD'
expected_output = 'hELLO wORLD'
output = flip_case(input_str)
assert output == expected_output
```

This way, you can ensure that the `flip_case` function accurately flips the case as described.