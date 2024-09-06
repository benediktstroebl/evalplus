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
1. `encode_shift` Function: This function takes a string `s` as input and encodes it by shifting each character by 5 in the alphabet. It does this by using the `ord()` function to get the ASCII value of each character and then calculating a new ASCII value by subtracting 97 (the ASCII value of 'a') and adding 5, ensuring that the result wraps around the alphabet range of 97 to 122 with the `% 26` operation. It then re-encodes the character using its new ASCII value by adding 97 again and converting it back to a character using `chr()`.
2. `decode_shift` Function: This function takes a string `s` encoded with the `encode_shift` function and decodes it. It reverses the encoding process by calculating the original ASCII value of each character, subtracting 5 (or adding 5 if the result would be less than 97), and then converting it back to a character. The main logic surrounds the conditional checks to ensure the ASCII value wraps around the correct range using `<` and `>` operators and the `% 26` arithmetic operation.

Remember to ensure consistent edge case handling for uppercase letters, numerals, and special characters to achieve the correct functionality of these functions. The provided script is a basic starting point and may require additional refinements based on specific edge cases and desired behavior for the encoding/decoding process.