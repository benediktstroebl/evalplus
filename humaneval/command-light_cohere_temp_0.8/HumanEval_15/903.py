```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test case 1: Test string generation for n=0
assertEqual(string_sequence(0), '0')

# Test case 2: Test string generation for n=5
assertEqual(string_sequence(5), '0 1 2 3 4 5')

# Test case 3: Test string generation for large n (should output exactly 10^6 + 4 digits)
assertEqual(string_sequence(1000000), '89999989898000')

# Test case 4: Test string generation for negative n (should raise error)
try:
    string_sequence(-1)
except ValueError:
    print("Test case 4: Expected ValueError")
```