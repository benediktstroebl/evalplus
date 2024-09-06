Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s [](str)([c => chr(ord(c) - 5 + ord("a")) for c in s])
```

The `encode_shift` function shifts each character of an input string `s` by 5 in the alphabet. The `decode_shift` function takes an encoded string and returns the decoded string based on the logic of the `encode_shift` function.