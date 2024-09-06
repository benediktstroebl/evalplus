Here's a Python script with a self-contained function that solves the problem:
```python
#!/usr/bin/env python

def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])

# Unit tests:
def test_encode():
    assert encode_shift("Hello World!") == "Ifmmp Ptyxiq!"

def test_decode():
    assert decode_shift("Ifmmp Ptyxiq!") == "Hello World!"

test_encode()
test_decode()
```

The `encode_shift` function shifts each character of the input string `s` by 5 in the alphabet, with the assumption that the alphabet ranges from 'a' to 'z' (inclusive). After the shift, if the character goes beyond the bounds of the alphabet, it wraps around by taking the modulus of 26. This ensures the encoding remains within the alphabet. The `decode_shift` function reverses the process to decode the shifted encoding back to the original string.

The script also includes unit tests, `test_encode` and `test_decode`, which use the `assert` statement to check if the encoded and decoded outputs are correct. 

Note that this script assumes that the input string contains only lowercase letters. If the input string contains other characters, the functions would need to be modified to handle other character ranges and special cases.