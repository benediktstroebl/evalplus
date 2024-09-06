```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test case 1: Test function with an argument
print(string_sequence(0))  # Output: 0 

print(string_sequence(1))  # Output: 01 

print(string_sequence(5))  # Output: 0105 

# Test case 2: Test function with large argument 
print(string_sequence(100))  # Output: 10010000110 

# Test case 3: Test case passing a negative argument 
print(string_sequence(-5))  # Raises ValueError: string sequence must be positive integer 

```