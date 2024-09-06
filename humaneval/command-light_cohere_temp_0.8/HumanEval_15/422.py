```python
def string_sequence(n: int) -> str:
    return f"0 {n}"*n

# Test the function with n = 0
test_string_sequence(0) # Output: '0'

# Test the function with n = 5
test_string_sequence(5) # Output: '0 1 2 3 4 5'

# Test the function with invalid input (n < 0)
try:
    test_string_sequence(-1)
except TypeError:
    print("Invalid input. The function should raise TypeError for invalid input")
```