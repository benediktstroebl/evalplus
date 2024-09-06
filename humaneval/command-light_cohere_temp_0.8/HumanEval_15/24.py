```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Test the function with different input values
test_sequence(5)  # This will print '0 1 2 3 4 5'
test_sequence(0)  # This will print '0'
test_sequence(-1) # This will raise ValueError
test_sequence(10) # This will raise ValueError
```