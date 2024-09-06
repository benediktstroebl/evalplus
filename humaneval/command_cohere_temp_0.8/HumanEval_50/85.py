Here's a Python script with a self-contained function that solves the problem you've described, along with a script to decode the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes the input string by shifting each character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes an input string encoded with the encode_shift function.
    """
    reverse_alphabet = {chr(i): chr(i - 5) for i in range(97, 123)}
    return "".join(reverse_alphabet.get(ch, ch) for ch in s)

# Tests
message = "Hello, World!"
encoded_message = encode_shift(message)
decoded_message = decode_shift(encoded_message)

print("Encoded Message:", encoded_message)
print("Decoded Message:", decoded_message)
```

This script defines the `encode_shift` and `decode_shift` functions as specified in the problem. The `encode_shift` function shifts each character of the input string by 5 in the alphabet, wrapping around if needed. The `decode_shift` function uses a dictionary `reverse_alphabet` to reverse the encoding by shifting each character back by 5.

The tests section includes an example message, encoding it, decoding the encoded message, and printing both the encoded and decoded messages. You can run this script to verify that the functions work as expected.