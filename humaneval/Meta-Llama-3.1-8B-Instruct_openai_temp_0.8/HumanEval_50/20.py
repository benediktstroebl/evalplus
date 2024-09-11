```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    The function works by first converting each character in the string to its ASCII value.
    It then adds 5 to the ASCII value, subtracts the ASCII value of 'a', takes the result modulo 26,
    and finally adds back the ASCII value of 'a' to shift the result to the correct position in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.

    The function works by first converting each character in the string to its ASCII value.
    It then subtracts 5 from the ASCII value, subtracts the ASCII value of 'a', takes the result modulo 26,
    and finally adds back the ASCII value of 'a' to shift the result to the correct position in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

# Test the functions
s = "Hello, World!"
encoded = encode_shift(s)
decoded = decode_shift(encoded)

print("Original String:", s)
print("Encoded String:", encoded)
print("Decoded String:", decoded)
```

In this code, the `encode_shift` function takes a string `s` as input, converts each character in the string to its ASCII value, adds 5 to the ASCII value, subtracts the ASCII value of 'a', takes the result modulo 26, and finally adds back the ASCII value of 'a' to shift the result to the correct position in the alphabet.

The `decode_shift` function works similarly, but it subtracts 5 instead of adding it, effectively reversing the shift operation.

Note that the code also checks if each character in the string is a letter using the `isalpha` method, to avoid trying to shift non-alphabetic characters.

Finally, the code includes a test at the end to demonstrate the functions' behavior.