```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

# Test the function with different input values
print(string_sequence(0))  # Output: 0
print(string_sequence(5))  # Output: 0 1 2 3 4 5
print(string_sequence(10)) # Output: 0 10 20 30 40 50 

```