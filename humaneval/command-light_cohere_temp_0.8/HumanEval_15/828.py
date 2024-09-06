```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending with n.

    If n is less than 0, raises IndexError.

    if n <= 0:
        return "Error: n must be a positive integer."

    if n == 0:
        return '0'

    # Generate numbers from 0 to n inclusive
    sequence = [0]
    while len(sequence) < n:
        sequence.append(sequence[-1] + 1)

    # Return the generated string
    return ' '.join(sequence)

# Test the function with different inputs
# Test with n = 0
test_string = string_sequence(0)
assert test_string == '0'

# Test with n = 5
test_string = string_sequence(5)
assert test_string == '0 1 2 3 4 5'

# Test with n = 20
test_string = string_sequence(20)
assert test_string == '0 20 39 46 63 80 91 ...'
```