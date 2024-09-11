```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.

    This function works by converting each character to its ASCII value, 
    shifting it by 5, and then converting it back to a character. 
    It handles both lowercase and uppercase letters, and non-alphabetic characters remain unchanged.

    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else chr(((ord(ch) - ord("A") + 5) % 26) + ord("A")) if ch.isalpha() and ch.isupper() 
                    else ch for ch in s])


def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.

    This function works by converting each character to its ASCII value, 
    subtracting 5, and then converting it back to a character. 
    It handles both lowercase and uppercase letters, and non-alphabetic characters remain unchanged.

    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) if ch.isalpha() and ch.islower() 
                    else chr(((ord(ch) - ord("A") - 5) % 26) + ord("A")) if ch.isalpha() and ch.isupper() 
                    else ch for ch in s])


# Example usage
if __name__ == "__main__":
    input_str = "Hello, World!"
    encoded_str = encode_shift(input_str)
    print(f"Encoded string: {encoded_str}")

    decoded_str = decode_shift(encoded_str)
    print(f"Decoded string: {decoded_str}")
```

In this code:

*   The `encode_shift` function takes a string as input and shifts every alphabetic character by 5 positions in the alphabet. It preserves the case of the original characters.
*   The `decode_shift` function takes an encoded string as input and reverses the shift operation to retrieve the original string.
*   The example usage at the end demonstrates how to use these functions with a sample input string.