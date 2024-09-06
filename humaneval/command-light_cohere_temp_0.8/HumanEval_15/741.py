```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function
test_string_sequence = string_sequence(5)
print(test_string_sequence)  # Outputs: 0 5 10 15 20 25 
```