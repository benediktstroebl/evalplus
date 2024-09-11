```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.

    This function assumes the input string only contains lowercase letters.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Test the functions
if __name__ == "__main__":
    original_string = "hello"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

In this code, the `encode_shift` function shifts each character in the input string by 5 positions in the alphabet. The `decode_shift` function reverses this process by shifting each character back by 5 positions.

The test at the end of the script demonstrates how these functions work. It takes an original string, encodes it, decodes it back, and prints the results. 

Note that this script assumes the input string only contains lowercase letters. If the input string contains uppercase letters or other characters, the script may not behave as expected.