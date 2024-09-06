```python
def flip_case(string: str) -> str:
    return ''.join_(c) if c.isupper(c) else c.islower(c)
    flip_case(string)

for letter in 'Hello world!' + '!cat':
    print(f"{letter} is flipped: {flip_case(letter)}")
```