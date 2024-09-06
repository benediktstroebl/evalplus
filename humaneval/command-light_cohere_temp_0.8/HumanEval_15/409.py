```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3}..."

# Test case 1: Test function with an invalid input (negative number)
 assert not str(string_sequence(-5)) == "Invalid input"

# Test case 2: Test function with valid input (positive number)
 assert string_sequence(5) == "0 5 6 7 8"
```