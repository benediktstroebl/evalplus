```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This code defines two functions: `encode_shift` and `decode_shift`. 

`encode_shift` takes a string `s` as input and returns the encoded string by shifting every character by 5 in the alphabet. Characters that go beyond the ASCII range of a to z (and lower case) will not give the correct result. The function uses a list comprehension to loop through each character in the input string. It utilizes the `ord()` function to get the ASCII value of each character and adds 5 to shift it in the alphabet. The function then performs a modulo operation to ensure that the shifted character still falls within the range of lowercase letters. It subtracts the original ASCII value from the shifted value, divides by 26 to remove the remainder, and then adds 'a' to get the new character. This new character is then appended to a string builder (an empty string joined with the list of characters) to form the final encoded string. 

`decode_shift` takes an encoded string s as input and returns the original decoded string. The function operates similarly to `encode_shift`, using a list comprehension to loop through each character in the input string. It uses the `ord()` function to get the ASCII value of each character and subtracts 'a' to undo the shift. The function then performs a modulo operation to ensure that the original character range is not exceeded. It adds the shifted value to the 'a' to get the new character and then appends it to a string builder (an empty string joined with the list of characters) to form the final decoded string. 

Please note that this code assumes that the input string contains only lowercase letters. Characters that are not in the range of 'a' to 'z' will not be correctly encoded or decoded.