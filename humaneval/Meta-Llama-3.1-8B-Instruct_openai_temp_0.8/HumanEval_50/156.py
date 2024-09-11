```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

# Testing the functions
text = "Hello, World!"
encoded_text = encode_shift(text)
decoded_text = decode_shift(encoded_text)

print(f"Original text: {text}")
print(f"Encoded text: {encoded_text}")
print(f"Decoded text: {decoded_text}")
```

In this script, we first define the `encode_shift` function, which shifts every character by 5 in the alphabet. We then define the `decode_shift` function, which reverses the `encode_shift` shift, effectively decoding the string.

We use the ASCII values of the characters and perform arithmetic operations on them to achieve the shift. The `ord` function gives the ASCII value of a character, and `chr` gives the character represented by a specific ASCII value.

We also use the `isalpha` method to check if a character is a letter, and the `lower` method to convert the string to lowercase, so that the shift works for both uppercase and lowercase letters.