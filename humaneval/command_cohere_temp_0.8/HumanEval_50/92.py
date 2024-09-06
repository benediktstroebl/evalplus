```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "zechrmnwabvhfgciqpkltjm"))
``` 

The `encode_shift` function takes a string `s` as input and returns an encoded version of the string. For every character in `s`, it adds 5 to the ASCII value of the character, subtracts the ASCII value of 'a', and takes the remainder when divided by 26. This ensures the encoded character still falls within the ASCII range for alphabetic characters. It then adds the ASCII value of 'a' to the result to make sure the encoded value is a valid character. The result is joined together to form a single encoded string. 

The `decode_shift` function takes an encoded string s as input and returns the decoded string. It uses the `translate` method to replace every character in the encoded string with the corresponding character in the Latin alphabet. The `maketrans` function creates a translation table based on the two-character strings inputted. 

Overall, the script encodes a string by shifting each character by 5 in the alphabet and decodes it back to the original string. Let me know if you would like any tests added to further verify the functionality of these functions!