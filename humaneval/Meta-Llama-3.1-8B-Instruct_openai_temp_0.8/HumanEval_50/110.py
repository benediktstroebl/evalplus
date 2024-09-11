```python
def encode_shift(s: str) -> str:
    """
    shifts every character in the string by 5 in the alphabet.
    
    This function uses the Caesar cipher technique to shift each character 
    in the input string by 5 positions in the alphabet. It assumes that the 
    input string only contains lowercase letters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str) -> str:
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function is the inverse of the encode_shift function. It assumes that 
    the input string only contains lowercase letters.

    Args:
        s (str): The input string to be decoded.

    Returns:
        str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage:
if __name__ == "__main__":
    original_string = "apple"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")
    
    assert original_string == decoded_string
```

This script includes two functions, `encode_shift` and `decode_shift`, which implement the Caesar cipher technique to shift characters by 5 positions in the alphabet. The `encode_shift` function shifts the characters to the right by 5 positions, and the `decode_shift` function shifts the characters to the left by 5 positions to recover the original string. The example usage demonstrates how to use these functions to encode and decode a string.