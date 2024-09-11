Here's a self-contained Python script that solves the problem:
```markdown
## Shift Encoding/Decoding Script
### Problem Description
Shift every character in the alphabet by 5 places in the alphabet.

### Solution
```python
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    
    Parameters:
    s (str): Input string to be encoded.
    
    Returns:
    str: Encoded string.
    """
    return "".join([chr(((ord(ch.lower()) + 5 - ord("a")) % 26) + ord("a")) for ch in s if ch.isalpha()]).lower()


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    
    Parameters:
    s (str): Input string to be decoded.
    
    Returns:
    str: Decoded string.
    """
    return "".join([chr(((ord(ch.lower()) - 5 - ord("a")) % 26) + ord("a")) for ch in s if ch.isalpha()]).lower()


# Example Use Cases
if __name__ == "__main__":
    encoded_str = encode_shift("Hello, World!")
    print(f"Encoded String: {encoded_str}")
    decoded_str = decode_shift(encoded_str)
    print(f"Decoded String: {decoded_str}")
```

### Explanation

The `encode_shift` function shifts every character in the alphabet by 5 places by taking the following steps:

1. Convert each character to lowercase to handle case-insensitive encoding.
2. Calculate the ASCII value of the shifted character by taking the remainder of the current character's ASCII value minus the ASCII value of 'a' plus 5, and then adding the ASCII value of 'a'.
3. Use the `chr` function to get the character represented by the calculated ASCII value.
4. Join all the shifted characters together into a single string.

The `decode_shift` function is similar to the `encode_shift` function but with the opposite shift of -5. This effectively reverses the encoding process.

The example use case demonstrates how to use these functions to encode and decode a string. The `if __name__ == "__main__":` block is used to ensure that the example use case only runs when the script is executed directly.