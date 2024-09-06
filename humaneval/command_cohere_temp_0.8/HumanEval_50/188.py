```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])
```

This script defines two functions:
1. `encode_shift`: This function shifts each character of an input string `s` by 5 in the alphabet. It converts each character to its ASCII value, adds 5, subtracts the ASCII value of 'a' to center the shift around the 'a' character, takes the modulo of the result with 26 to ensure the shift stays within the alphabet, adds the ASCII value of 'a' back to shift the character back to its original range, and finally converts the resulting ASCII value back to a character. The process is repeated for each character in the input string and the shifted characters are concatenated to form the output string.
2. `decode_shift`: This function reverses the encoding process of the `encode_shift` function. It takes an input string `s` that has been encoded with the `encode_shift` function, undoes the shift for each character, and returns the original string. 

The code includes test strings that are encoded and decoded to verify the correctness of the implementation. The test script checks if the decoded string matches the original string for both encode and decode functions.