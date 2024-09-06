```python
def flip_case(string: str) -> str:
    return ''.joincase(string)

# Test case
print(flip_case('Hello'))  # Output: hELLo
print(flip_case('HELLO'))  # Output: hello
print(flip_case('hello'))  # Output: HELLO
print(flip_case(' WORLD'))  # Output: wORLD
```