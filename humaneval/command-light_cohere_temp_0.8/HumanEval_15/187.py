```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different values of n
test_seq = string_sequence(0)
print("Test with n=0:", test_seq)

test_seq = string_sequence(5)
print("Test with n=5:", test_seq)

# Test the function with invalid input (negative value)
try:
    test_seq = string_sequence(-1)
except Exception as e:
    print(f"Error occurred: {e}")

# Test the function with invalid input (non-integer)
try:
    test_seq = string_sequence("abc")
except Exception as e:
    print(f"Error occurred: {e}")
```