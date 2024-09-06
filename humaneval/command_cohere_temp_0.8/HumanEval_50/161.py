```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) + ord("a")) for ch in s])
```

This code defines two functions: `encode_shift` and `decode_shift`. 

The `encode_shift` function takes a string `s` as input and returns a new string that has every character shifted by 5 in the alphabet. This is achieved by taking the ordinal value of each character, adding 5, subtracting the ordinal value of 'a' to translate it to a numerical value for the shift, and then taking the remainder when divided by 26 to ensure the shift doesn't go beyond the bounds of the alphabet. The shifted character is then encoded back into a character using its numerical value added with the ordinal value of 'a'. This process is carried out for each character in the input string, and the resulting shifted characters are concatenated together to form the output string.

The `decode_shift` function takes a string s as input and returns a new string with each character decoded back to its original form. It achieves this by reversing the encoding process in the `encode_shift` function. 

Overall, this script provides a way to encode a string by shifting each character by 5 in the alphabet and also provides a way to decode it back to the original string.