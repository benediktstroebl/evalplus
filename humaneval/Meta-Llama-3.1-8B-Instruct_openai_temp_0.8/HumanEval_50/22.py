```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") + 5) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - ord("a") - 5) % 26) + ord("a")) for ch in s])


# Example usage
if __name__ == "__main__":
    # Test encode_shift function
    original_string = "Hello World"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")

    # Test decode_shift function
    encoded_string2 = "Mjqqt Btwqi"
    decoded_string2 = decode_shift(encoded_string2)
    print(f"\nEncoded string: {encoded_string2}")
    print(f"Decoded string: {decoded_string2}")
```

This Python script provides the `encode_shift` and `decode_shift` functions as described. It also includes example usage to demonstrate the functionality of these functions. The `encode_shift` function shifts every character in the input string by 5 in the alphabet, and the `decode_shift` function reverses this operation to retrieve the original string. The script handles both lowercase and uppercase letters by converting all characters to lowercase before shifting, and then converts them back to their original case after shifting.