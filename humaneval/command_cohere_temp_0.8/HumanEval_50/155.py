```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This script defines two functions:
- `encode_shift` — Shifts every character in a string by 5 in the alphabet.
- `decode_shift` — Decodes a string that was encoded with the `encode_shift` function. 

The `encode_shift` function first converts each character `ch` in the input string `s` to its ASCII value using the `ord` function. It then adds 5 and subtracts the ASCII value of 'a' to shift each character by 5 in the alphabet. The result is rolled back to the range of ASCII values for alphabetic characters using the modulo operator, with a wrap-around to ensure the shifted character remains an alphabetic character. It converts the resulting numeric value back to a character using the `chr` function and recursively joins the resulting string parts into a single string, effectively returning the encoded string. 

The `decode_shift` function follows the same logic but in reverse. It shifts back each character by 5 in the alphabet, converting them back to their original values before stitching them together into a single decoded string. 

Please note that these functions do not validate the input other than ensuring the correctness of the encoded/decoded values within the alphabetic range. Additional input validation and error handling may be required depending on the specific use case and the type of input expected.