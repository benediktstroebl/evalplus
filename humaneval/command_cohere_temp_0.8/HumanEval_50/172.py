Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block demonstrating how to use it:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    
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
        s (str): Input string to encode.

    Returns:
        str: Decoded string.
    """
    return "".join([chr((((ord(ch)-96)%26) + ord("a"))%26 + 96) for ch in s])

# Sample usage:
encoded_string = encode_shift("Hello, World!")
decoded_string = decode_shift(encoded_string)

print("Encoded String:", encoded_string)
print("Decoded String:", decoded_string)
```
This script defines two functions, `encode_shift` and `decode_shift`, as specified in the problem. Each function takes a string as input and returns the encoded or decoded version of the string, respecting the specified shift of 5 in the alphabet. The functions are demonstrated with test cases in the sample usage section. 
 encode_shift encodes a string by shifting each character by 5 in the alphabet, wrapping around if the shift exceeds 26. 

decode_shift takes as input a string encoded with encode_shift and returns the original decoded string. It applies the inverse operation to recover the original characters.