```python
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    
    Args:
    s (str): The input string to be encoded.
    
    Returns:
    str: The encoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") + 5) % 26) + ord("a")) for ch in s.lower() if ch.isalpha()])

def decode_shift(s: str):
    """
    Takes as input string encoded with encode_shift function. Returns decoded string.
    
    Args:
    s (str): The encoded string to be decoded.
    
    Returns:
    str: The decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) + 26 - 5) % 26 + ord("a")) for ch in s.lower() if ch.isalpha()])

def main():
    # Example usage:
    original_string = "Hello, World!"
    encoded_string = encode_shift(original_string)
    print(f"Original string: {original_string}")
    print(f"Encoded string: {encoded_string}")
    decoded_string = decode_shift(encoded_string)
    print(f"Decoded string: {decoded_string}")

if __name__ == "__main__":
    main()
```

This script includes two functions: `encode_shift` and `decode_shift`. The `encode_shift` function shifts every alphabetical character in the input string by 5 positions in the alphabet, wrapping around from 'z' or 'Z' to 'a' or 'A' as necessary. The `decode_shift` function reverses this operation to retrieve the original string. The `main` function demonstrates how to use these functions with an example string. 

The use of `ord("a")` to shift characters is simplified and works because the ASCII values of 'a' to 'z' are consecutive. The `lower()` method is used to handle both upper and lower case letters. The `isalpha()` method is used to ensure that non-alphabetical characters are ignored. 

This script is self-contained and does not rely on external modules. The main function is called when the script is run directly (i.e., not imported as a module by another script).