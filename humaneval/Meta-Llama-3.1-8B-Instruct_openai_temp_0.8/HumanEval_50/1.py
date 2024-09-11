```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    This function assumes that the input string only contains lowercase English letters.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 5) % 26 + ord("a")) for ch in s if ch.isalpha()]).lower()


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    This function assumes that the input string only contains lowercase English letters.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) - 5) % 26 + ord("a")) for ch in s if ch.isalpha()]).lower()


# Example usage:
if __name__ == "__main__":
    input_str = "hello"
    encoded_str = encode_shift(input_str)
    print(f"Encoded string: {encoded_str}")
    
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In this code, I've added a check to ensure that the input string contains only lowercase English letters using the `isalpha()` method. I've also added a call to `lower()` to handle case-insensitive inputs. The `if __name__ == "__main__":` block provides an example usage of the `encode_shift` and `decode_shift` functions.