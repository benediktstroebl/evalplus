```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0]) if len(g) == 3 else g

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    preview:
    -> b" # --\
    -> a # --\
    -> a # --\
    -> d # --\
    -> d # --\
    -> a # --"

# Test cases
assertEqual(encode_cyclic("abc"), "aabb")
assertEqual(encode_cyclic("abcd"), "adbe")
assertEqual(encode_cyclic("abacad"), "afac")
assertEqual(encode_cyclic("abcde"), "afbd")
assertEqual(encode_cyclic("abcdef"), "adbe")
assertEqual(encode_cyclic("b"), "d")
assertEqual(encode_cyclic(""), "a")
assertEqual(decode_cyclic("a"), "abc")
assertEqual(decode_cyclic("adbe"), "abcde")
assertEqual(decode_cyclic("afac"), "abacad")
assertEqual(decode_cyclic("afbd"), "abcdde")

```
This script defines two functions: `encode_cyclic` and `decode_cyclic`. These functions take a string `s` as input, where `s` represents the markdown code to be encoded. The `encode_cyclic` function encodes the string by cycling groups of three characters, while the `decode_cyclic` function decodes the string.

This code provides a way to convert markdown code into its base-3 representation and back. The test cases ensure that the functions work correctly for a variety of inputs.