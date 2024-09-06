Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded message:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.

    Args:
        s (str): The input encoded string.

    Returns:
        str: The decoded string.
    """
    reverse_alphabet = {chr(i): chr(i - 5) for i in range(97, 123)}
    return "".join(reverse_alphabet.get(ch, ch) for ch in s)
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes an input string and shifts each character by 5 in the alphabet, with a wrap-around to the beginning of the alphabet if the character exceeds 'z'. The `decode_shift` function takes an input string encoded with `encode_shift` and returns the original message by shifting each character back by 5. 

The decoding process utilizes a reverse alphabet map, and the `get` method is used to replace each encoded character with its corresponding decoded character or retain the original character if it is not in the map. 

Note: The script assumes that the input string contains only alphabetic characters. If the input contains non-alphabetic characters, the encoding/decoding process will ignore them.