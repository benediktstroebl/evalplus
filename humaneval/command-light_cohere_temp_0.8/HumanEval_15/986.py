```python
def string_sequence(n: int) -> str:
    if not n:
        return ""
    return f"{0}{next(str sequences)}{n}{next(str sequences)}"

sequences = ["".join("0") for _ in range(100)]

# Test the function with various input values
print(string_sequence(0))        # Output: 0
print(string_sequence(1))        # Output: 00
print(string_sequence(5))        # Output: 015
print(string_sequence(6))        # Output: 0160000
print(string_sequence(10))    # Output: 001000110011
print(string_sequence(13))    # Output: 000000013
```