```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different values of n
assert(str(string_sequence(0)) == '0'), "Function didn't return 0"
assert(str(string_sequence(1)) == '1'), "Function didn't return 1"
assert(str(string_sequence(5)) == '0 1 2 3 4 5'), "Function didn't return correct sequence"
assert(str(string_sequence(10)) == '0 9 8 7 6 5 4 3 2 1'), "Function didn't return correct sequence"
```