Here's a Python script with a self-contained function that solves the problem you've described, along with a script to decode the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character 5 places up in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in s])

# Example usage
message = "Hello, World!"
encoded_message = encode_shift(message)
print("Encoded message:", encoded_message)

decoded_message = decode_shift(encoded_message)
print("Decoded message:", decoded_message)
```

This script defines the `encode_shift` and `decode_shift` functions, each working on a single string argument. `encode_shift` shifts each character in the string 5 places up in the alphabet, wrapping around if needed, while `decode_shift` shifts each character back by 5 places to recover the original message.

The script then provides an example usage of these functions, encoding and decoding the message "Hello, World!". The output will show the encoded message and the decoded message.