Here's a Python script with a self-contained function that solves the problem you've described, along with a separate function for decoding the encoded string:
```python
def encode_shift(s: str):
    """
    Encodes a string by shifting each character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    """
    reverse_alphabet = {chr(i): chr(i - 5 if i >= 'e' else i + 5) for i in range(97, 123)}
    return "".join(reverse_alphabet.get(ch, ch) for ch in s)
```

This script defines two functions, `encode_shift` and `decode_shift`. The `encode_shift` function takes a string as input and returns the encoded version of the string, where each character is shifted by 5 in the alphabet. The `decode_shift` function takes an encoded string as input and returns the decoded string. You can use these functions together to encode and decode strings as needed. 

The encoding process amends the characters in the string accordingly:
- 'a' becomes 'f'
- 'b' becomes 'g'
- 'c' becomes 'h'
- 'd' becomes 'i'
- 'e' becomes 'j'
- 'f' becomes 'k'
- 'g' becomes 'l'
- 'h' becomes 'm'
- 'i' becomes 'n'
- 'j' becomes 'o'
- 'k' becomes 'p'
- 'l' becomes 'q'
- 'm' becomes 'r'
- 'n' becomes 's'
- 'o' becomes 't'
- 'p' becomes 'u'
- 'q' becomes 'v'
- 'r' becomes 'w'
- 's' becomes 'x'
- 't' becomes 'y'
- 'u' becomes 'z'
- 'v' becomes 'a'
- 'w' becomes 'b'
- 'x' becomes 'c'
- 'y' becomes 'd'
- 'z' becomes 'e'

And the decoding process reverses the encoding scheme to obtain the original string.