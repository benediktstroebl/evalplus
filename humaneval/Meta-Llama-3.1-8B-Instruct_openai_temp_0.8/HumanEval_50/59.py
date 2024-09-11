```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The input string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) if ch.isalpha() else ch for ch in s]).lower()


# Test the functions
if __name__ == "__main__":
    test_string = "HelloWorld"
    encoded_string = encode_shift(test_string)
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
```

This script solves the problem by implementing both the `encode_shift` and `decode_shift` functions. The `encode_shift` function takes a string `s` as input, shifts every character by 5 in the alphabet, and returns the encoded string. The `decode_shift` function works the opposite way, decoding the input string by shifting every character in the opposite direction.

Note that the script also includes a test at the end to verify that the `encode_shift` and `decode_shift` functions are working correctly. The test takes a string "HelloWorld", encodes it, decodes it, and prints the original and decoded strings.