```python
def string_sequence(n: int) -> str:
    if n <= 0:
        raise ValueError("n must be a positive integer")
        
    string_seq = [i+1 for i in range(n+1)]
    return " ".join(string_seq)

# basic test cases
print(string_sequence(0))
print(string_sequence(5))

# check with different n values to make sure the function works for all valid inputs
print(string_sequence(-5))
print(string_sequence(2.5))
```