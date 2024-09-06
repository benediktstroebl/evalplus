```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This code defines two functions: `encode_shift` and `decode_shift`. 

The `encode_shift` function takes a string `s` as input and returns a new string that has every character shifted by 5 in the alphabet. This is achieved by taking the ordinal value of each character, adding 5 (to account for the shift), and then taking modulo 26 to wrap the value around to the alphabet range. The resultant value is then added to ord('a') to get the shifted character. This is done for every character in the string and the results are concatenated together to form the output string.

The `decode_shift` function is designed to decode a string that was previously encoded using the `encode_shift` function. It works by reversing the encoding process. The ordinal value of each character is reduced by ord('a'), and then taking modulo 26 to wrap the value within the alphabet range. The shifted character is decoded by taking modulo 26 again, which effectively subtracts the shifted amount (of 5) and wraps it back to the original alphabet. The resultant value is then converted back to a character using the ordinal value. This process is applied to every character in the input string, and the decoded characters are concatenated together to form the output string.