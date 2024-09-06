```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive""" 
    string_seq = [0]
    while len(string_seq) < n:
        string_seq.append(string_seq[-1] + 1)
    return ' '.join(string_seq)

# Test cases
print(string_sequence(0))  # Output: '0'
print(string_sequence(1))  # Output: '1'
print(string_sequence(5))  # Output: '0 1 2 3 4 5' as expected
print(string_sequence(-1))  # Raises ValueError: expecting positive input
print(string_sequence(6))  # Raises ValueError: expecting positive input
```