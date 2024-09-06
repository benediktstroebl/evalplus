```python
def flip_case(string):
    return ''.join(''.swapcase(c) for c in string))

# Test the function with some strings
print(flip_case('hello'))  # HELLO
print(flip_case('World'))  # wORLD
print(flip_case('Three'))  # thrUEree
print(flip_case('rob'))  # BOrd
print(flip_case('Slow'))  # Slow
```