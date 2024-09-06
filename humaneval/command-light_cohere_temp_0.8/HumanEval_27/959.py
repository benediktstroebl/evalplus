```python
def flip_case(string: str) -> str:
    return ''.join(c if c.isupper() else(c.islower()) else c.isupper() else(c) else c.c for c in string)
```

# Test cases
print(flip_case('hello'))  # Output: 'Hello'
print(flip_case('world'))  # Output: 'WoRDl!'
print(flip_case('to be or not'))  # Output: 'toBeOrNot'
print(flip_case('hello World'))  # Output: 'Hllow WoRLd'
```