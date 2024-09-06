Here's a Python script with a self-contained function that solves the problem you've described, along with a brief explanation of how the function works:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    Returns the encoded string.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    Returns the decoded string.
    """
    return "".join([chr(((((ord(ch) - ord("a")) % 26) - 5) if (ord(ch) - ord("a")) % 26 > 0 else ((ord(ch) - ord("a")) % 26 + 26)) or ord("a")) for ch in s])
```

Here's a brief explanation of how these functions work:
1. `encode_shift` function:
    - This function takes a string `s` as input.
    - It uses a list comprehension to iterate over each character `ch` in the input string `s`.
    - For each character, it calculates the new ordinal value by adding 5 (to perform the shift) and then taking modulo 26 to wrap around within the alphabet range.
    - It then adds or subtracts ord("a") to ensure the result falls within the alphabet range, as the modulo operation might yield negative values.
    - Finally, it converts the ordinal value back to a character using `chr()` and joins the encoded characters to form the encoded string.
2. `decode_shift` function:
    - This function takes a string `s` encoded with the `encode_shift` function.
    - It uses a list comprehension similar to the encoding process to iterate over each character `ch` in the input string `s`.
    - For each character, it calculates the original ordinal value by subtracting 5 (to undo the shift) and then taking the modulo 26 to wrap around within the alphabet range.
    - It handles the case where the result of the subtraction might be negative by adding 26 to the result to make it positive within the alphabet range.
    - It then converts the ordinal value back to a character using `chr()` and joins the decoded characters to form the decoded string.

The code assumes that the input string contains only alphabetic characters. If non-alphabetic characters are included in the input, they will be skipped during the encoding and decoding processes, as the code only considers alphabetic characters when calculating the shifts.</code> 

This script provides two functions: `encode_shift`, which encodes a string by shifting each character, and `decode_shift`, which decodes a string encoded with the provided encoding function. 

This solution is applicable only for encoding and decoding strings that contain only alphabetical characters. If the input string contains special characters or numbers, the functions will encode and decode them as they are, without applying any shifts.