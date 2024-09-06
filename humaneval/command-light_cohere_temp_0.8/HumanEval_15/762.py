```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n))

# Test the function with different inputs
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(str_sequence(5), '0123456789')
assertEqual(string_sequence(10), '00000102030405060708090image')
```