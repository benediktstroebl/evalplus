```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}{' ' * (n - 1)}{n+1}"

# Test the function with different inputs
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(string_sequence(-5), '0 0 0 0 0')
assertEqual(string_sequence(0), '0 ')
assertEqual(string_sequence(1), '1')
# How did that go? : Let me know if I can help you with anything else.