```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n-1)}{n+1}"

# Basic test cases
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(string_sequence(-1), '') # Error: Negative test passed

# Edge cases with input < 1
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(-2), '')

# Edge cases with input > 4
assertEqual(string_sequence(7), '0 7 8 9')
assertEqual(string_sequence(5), '0 5 6 7 8')

# Edge cases with very high values
assertEqual(string_sequence(50), '0 50 51 52 53 54 55')
assertEqual(string_sequence(100), '0 100 101 102 103 104 105')

```