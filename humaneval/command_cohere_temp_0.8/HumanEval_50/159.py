```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])
```

This script defines two functions:
1. `encode_shift`: This function shifts each character of the input string `s` by 5 in the alphabet. It converts each character to its ASCII value, adds 5, subtracts the ASCII value of 'a' to center the shift around the 'a' character, takes the modulus 26 to wrap around to the ASCII range, and adds the ASCII value of 'a' again to get the shifted character. It then joins these shifted characters to form the encoded string and returns the result. 
2. `decode_shift`: This function takes an encoded string s created by the `encode_shift` function as input. It undoes the shift by subtracting 5 from the character's ASCII value, taking the modulus 26 to wrap around to the ASCII range, adding the ASCII value of 'a' to obtain the original character, and joining these characters to form the decoded string. 

Overall, this script provides a pair of functions that encode a string by shifting each character by 5 in the alphabet and decode it back to its original form.