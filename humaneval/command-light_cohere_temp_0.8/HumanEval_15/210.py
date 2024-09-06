```python
def string_sequence(n: int) -> str:
    if n <= 0:
        raise ValueError("n should be a positive integer")
        
    return " ".join([f" {i} " for i in range(n)])

# Test the function
test_string_sequence = string_sequence(5)
print(test_string_sequence)
```