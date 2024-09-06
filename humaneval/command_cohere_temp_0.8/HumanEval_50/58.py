```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - ord("a")) % 26) + ord("a")) - 5) % 26) for ch in s])
```

This script defines two functions:
1. `encode_shift`: This function shifts each character of an input string `s` by 5 in the alphabet. It returns the encoded string.
2. `decode_shift`: This function takes an encoded string as input and returns the decoded string. It reverses the encoding process of `encode_shift`. 

You can use these functions to encode and decode strings as per your requirement.