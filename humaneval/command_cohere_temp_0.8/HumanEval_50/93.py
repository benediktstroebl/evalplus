Here's a Python script with a self-contained function that solves the problem you've described, along with a markdown code block showing the full solution:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting every character by 5 in the alphabet.
    
    Args:
        s (str): Input string to be encoded.

    Returns:
        str: Encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    
    Args:
        s (str): Input string to be decoded.

    Returns:
        str: Decoded string.
    """
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) for ch in s])

# Sample usage:
def main():
    original_str = "Hello, World!"
    encoded_str = encode_shift(original_str)
    decoded_str = decode_shift(encoded_str)
    
    print("Original String:", original_str)
    print("Encoded String:", encoded_str)
    print("Decoded String:", decoded_str)

if __name__ == "__main__":
    main()
```
This script defines the `encode_shift` and `decode_shift` functions as specified in the problem statement. It also includes a `main` function to demonstrate the encoding and decoding process with the example string "Hello, World!". When you run the script, it will show the original string, the encoded string, and the decoded string as output.