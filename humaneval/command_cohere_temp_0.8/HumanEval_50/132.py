Here's a Python script with a self-contained function that solves the problem:
```python
def encode_shift(s: str):
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "ijklmnopqrstuvwxyzabcdefgh"))
```

The `encode_shift` function shifts each character of the input string `s` by 5 in the alphabet. It calculates the new character code by adding 5 to the original character code, handling wraparounds by taking the modulus of the difference between the new and original character codes and the alphabet size (`26`). It then adds the difference between the new and original character codes and the character code "a" to ensure the new character is in the correct alphabet range. The resulting character code is then converted to a character using `chr()`.

The `decode_shift` function decodes a string encoded with the `encode_shift` function. It uses the `translate` method with a custom translation table created using `str.maketrans()` to reverse the shift operation and return the original string.

These functions can be used to encode and decode strings using the shift cipher described in the problem statement.