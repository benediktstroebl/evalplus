```python
def flip_case(string: str) -> str:
    return ''.joinnamecase(string) if string is not None else string

# Test cases
print(flip_case('hello'))
print(flip_case('world'))
print(flip_case('Hello'))
print(flip_case('world!'))
print(flip_case('  HeLLo'))
```