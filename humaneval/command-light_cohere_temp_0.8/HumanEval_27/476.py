```python
def flip_case(string: str) -> str:
    new_str = ''.join([c if c.isupper() else upper() else c.islower() lower() else c) for c in string])
    return new_str

# Test cases
string1 = "hello"
string2 = "hello World"
print(flip_case(string1))  # Output: HELLo
print(flip_case(string2))  # Output: hELLo Wroollll
```