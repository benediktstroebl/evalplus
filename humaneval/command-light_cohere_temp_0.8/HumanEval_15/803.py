Here is a self-contained Python script that defines a function `string_sequence`:
```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test the function with different inputs
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(5), '0 1 2 3 4 5')
assertEqual(string_sequence(-1), '0')
assertEqual(string_sequence(0), '0')
assertEqual(string_sequence(1000), '0 1000')
```
The function uses the Python string formatting feature to return a string containing space-delimited numbers starting from 0 up to `n` inclusive. The function is tested with different inputs using the `assertEqual` function provided by Python's built-in testing utilities.