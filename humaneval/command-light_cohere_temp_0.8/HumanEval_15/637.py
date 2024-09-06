```python
def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("n must be a positive integer")
    if n == 0:
        return '0'
    string_seq = [0]
    for i in range(1, n+1):
        string_seq.append(str(i))
    return ' '.join(string_seq)

# Test the function with n = 5
string_sequence(5)
# '0 1 2 3 4 5'

# Test the function with n = 0
string_sequence(0)
# '0'

# Test the function with invalid n (non-positive integer)
try:
    string_sequence(-5)
except ValueError as e:
    print(f"Error: {e}")
```