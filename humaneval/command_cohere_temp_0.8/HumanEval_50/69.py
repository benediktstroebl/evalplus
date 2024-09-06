```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr((((ord(ch) - ord("a")) % 26) + ord("a")) % 26) for ch in s])
```

This script defines two functions:
1. `encode_shift`: This function shifts each character of an input string `s` by 5 in the alphabet. It returns the encoded string.
2. `decode_shift`: This function takes an encoded string as input and returns the decoded string. It reverses the encoding process of `encode_shift`. 

Both functions operate on the principle of shifting characters in the alphabet. The shifted character is calculated using the formula:
```
(original_character - 'a' ) + ('a' - 1) + ('a' - 1) + ... + ('a' - 1) 
```

Which simplifies to:
```
(original_character - 'a') % 26 
```

In the encoded string, each character will be shifted by 5 in the alphabet. For example, if the input string is "Hello", the encoded output would be “Ifmmp”. 

The decoding function reverses this process, shifting each character back by 5 in the alphabet to recover the original string. 

Note that this encoding/decoding system only works with English characters, as the 'a' in the shift formula refers to the ASCII value of the lowercase 'a'. Non-English characters will not decode correctly. 

The code assumes that the input string only contains English characters and punctuation, as the shift function was defined for the English alphabet range 'a' to 'z'.