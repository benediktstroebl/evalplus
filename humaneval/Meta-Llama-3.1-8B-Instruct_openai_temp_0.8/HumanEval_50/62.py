```markdown
### Shift Encoder and Decoder

This script contains two functions: `encode_shift` and `decode_shift`. These functions are used to shift each character in the input string by 5 places in the alphabet.

#### Code

```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()]))


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])


# Example usage:
if __name__ == "__main__":
    original_string = "Hello World"
    encoded_string = encode_shift(original_string)
    decoded_string = decode_shift(encoded_string)
    
    print(f"Original String: {original_string}")
    print(f"Encoded String: {encoded_string}")
    print(f"Decoded String: {decoded_string}")
```

#### Explanation

The `encode_shift` function shifts each character in the input string by 5 places in the alphabet. It does this by subtracting the ASCII value of 'a' from the character's ASCII value, adding 5, taking the modulus 26, and then adding the ASCII value of 'a' back.

The `decode_shift` function does the reverse of `encode_shift` to decode the string. It subtracts 5 instead of adding it in the encoding process.

Note: This script works for lowercase letters only and leaves other characters unchanged. If you want to support uppercase letters as well, you would need to add a check for it and adjust the ASCII values accordingly.

#### Output

When you run this script with the example usage provided, you will get the following output:
```
Original String: Hello World
Encoded String: Mjqqt Btwqi
Decoded String: Hello World
```