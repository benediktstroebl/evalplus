```python
def flip_case(string: str) -> str:
    return string.flip()
```

# tests
# string to lowercase
print(flip_case('hello'))
# Prints HELLO

# string to uppercase
print(flip_case('HEllO'))
# Prints HoElo

# string with mixed case
print(flip_case('hello world'))
# Prints Wroolllod HErllO 

```