Here's a Python script with a self-contained function that solves the problem:
```python
#!: encoding and decoding python 3 function
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a"))% 26) + ord("a"))% 26) ) for ch in s])
```
This script contains two functions: `encode_shift` and `decode_shift`. 

The `encode_shift` function shifts every character in a given string by 5 in the alphabet. It returns an encoded string containing the shifted characters. 

The `decode_shift` function takes an encoded string (produced by the `encode_shift` function), and returns the original decoded string. 

This solution is applicable for encoding and decoding any string using the specified shift. Let's break down the solution further:
### Function: encode_shift
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])
```
This function takes a string `s` as input. It returns a new string as the encoded version of the input string after shifting each character by 5 in the alphabet. 

Here's how this function works:
1. The input string is iterated character by character using a for loop. 
2. For each character `ch` in the input string:
- The Unicode code point (i.e., the character's ASCII value) of `ch` is obtained using the `ord()` function.
- The character is shifted by 5 in the alphabet. This is done by subtracting 97 (the ASCII value of 'a') and then adding 5. This operation is performed while handling rollover scenarios using the modulo operator (`% 26`).
- The shifted character is then reconstructed back to a Unicode code point using the `chr()` function. This function takes a numeric value (code point) and returns the corresponding character. 
- The reconstructed shifted character is then added to a new string being built to hold the encoded result. This is done using the `join` method of the string literals. 

The encoded string is returned as the result. 

### Function: decode_shift
```python
def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a"))% 26) + ord("a"))% 26) ) for ch in s])
```

This function also takes a string `s` as input. It returns a new string as the decoded version of the input string, which was presumably encoded using the `encode_shift` function. 

Here's how this function works:
1. The input string is iterated character by character using a for loop. 
2. For each character `ch` in the input string:
- The Unicode code point (i.e., the character's ASCII value) of `ch` is obtained using the `ord()` function.
- The character is shifted back to its original position by subtracting it from the ASCII value of 'a' and then re-adding it. This operation is performed while handling rollover scenarios using the modulo operator (`% 26`). 
- The shifted character is then reconstructed back to a Unicode code point using the `chr()` function, as in the `encode_shift` function. 
-