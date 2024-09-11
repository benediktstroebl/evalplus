### Caesar Cipher Implementation
#### Encoding and Decoding Strings with a Shift of 5

Here is a Python script that implements the `encode_shift` and `decode_shift` functions using the Caesar cipher algorithm with a shift of 5.

```markdown
```python
def encode_shift(s: str):
    """
    Encodes the input string by shifting every character by 5 in the alphabet.
    
    :param s: The input string to be encoded.
    :return: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() else ch 
                    for ch in s.lower()])


def decode_shift(s: str):
    """
    Decodes the input string that was encoded with the `encode_shift` function.
    
    :param s: The encoded string to be decoded.
    :return: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() else ch 
                    for ch in s.lower()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print("Original String:", original_string)
    print("Encoded String:", encoded_string)
    print("Decoded String:", decoded_string)
```

This script defines two functions: `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input, shifts each character by 5 in the alphabet, and returns the encoded string. The `decode_shift` function takes an encoded string as input and shifts each character back by 5 to obtain the original string.

The script also includes example usage to demonstrate the functionality of the `encode_shift` and `decode_shift` functions. 

Note that this implementation only shifts lowercase letters and leaves all other characters (such as uppercase letters, numbers, and special characters) unchanged. 

The `% 26` operation ensures that the shift wraps around the alphabet when necessary, so 'z' shifted by 5 becomes 'e', not some other character. 

This implementation uses the ASCII values of the characters to perform the shift, assuming that the input string only contains ASCII characters. If the input string may contain non-ASCII characters, the implementation would need to be modified accordingly.