Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded string:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the `encode_shift` function.
    """
    reverse_alpha_map = {chr(i): chr(i - 5) for i in range(97, 123)}
    return "".join([reverse_alpha_map.get(ch, ch) for ch in s])
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns the encoded version of the string, where each character is shifted by 5 in the alphabet. The `decode_shift` function takes a string as input and returns the decoded string, using a dictionary (`reverse_alpha_map`) to map encoded characters back to their original counterparts. The dictionary mapping is done between the range of 'a' to 'x' in the alphabet, subtracting 5 to reverse the shift.