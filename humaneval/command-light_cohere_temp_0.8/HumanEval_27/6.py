```python
def flip_case(string: str) -> str:
    new_string = ""
    for c in string:
        if c.isupper():  #." mates with "a", "A" or "AE" and c.
        new_string += c.islower():  #remains as-c-
        else:
            new_string += c.islower()
    words that remain in the original string, with the uppercased letter, but with a lowercase letter.

# Example Test
print(flip_case('hello'))
print(flip_case('HEllO'))
```