```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

#Test cases
print(string_sequence(0))      # Output: 0
print(string_sequence(1))      # Output: 01
print(string_sequence(3))      # Output: 0123
print(string_sequence(6))      # Output: 0123456789
print(string_sequence(10))    # Output: 01234678910
print(string_sequence(15))    # Output: 0101010101

```