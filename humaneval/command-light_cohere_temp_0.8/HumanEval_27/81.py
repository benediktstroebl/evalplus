```python
def flip_case(string):
    return ''.join(). plain ''.join(c.lower() if c.isupper(string)) for c in string)

# Tests:
print(flip_case('Hello'))  # Output: HELLO
print(flip_case('HELLo'))  # Output: hELLo
print(flip_case('hello World!!!!%0a%0'))  # Output: hEol0W!oo0
```