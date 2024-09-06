Here's a Python script with a self-contained function that solves the problem:
```python
# markdown cell
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - 96) % 26) + 96) % 26) + ord("a")) for ch in s])
```

The `encode_shift` function shifts every character in a given string by 5 in the alphabet, whereas the `decode_shift` function takes an encoded string from the `encode_shift` function and returns the original decoded string. 

Both functions are self-contained and do not rely on external variables or functions. They can be used independently to encode and decode strings respectively.