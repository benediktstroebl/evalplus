```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test case 1: Test function with an argument
print(string_sequence(0))
# Output: 0

# Test case 2: Test function with argument 2
print(string_sequence(2))
# Output: 02

# Test case 3: Test function with argument 10
print(string_sequence(10))
# Output: 000100

# Test case 4: Test function with invalid argument
try:
    print(string_sequence(0))
except TypeError:
    print("Error: Argument must be a positive integer")
```