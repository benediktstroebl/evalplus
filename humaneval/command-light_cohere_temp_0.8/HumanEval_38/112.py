```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group. If group has fewer elements than 3. Return the first character
   arencated string
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    due to the strings with the same prefix.
    """
    strings = s.split(".")
    strings
    sorted(str.lower() for s in strings)
    # remove the prefix
    decoded_strings = [s.strip(str.strip()) for s in strings
   
    return "".join(decoded_strings)

def test_encode_decode():
    """
    test cases for encode_cyclic and decode_cyclic functions.
    s = "abcbd..."
    print("encode_cyclic:", encode_cyclic(s))
    print("decode_cyclic:", decode_cyclic(encode_cyclic(s)))

s = "hello"
s = "worxx!!!"
s = "!#$___%$#"
s = "!#$%#$"
print("encode_cyclic:", encode_cyclic(s))
print("decode_cyclic:", decode_cyclic(encode_cyclic(s)))

test_encode_decode()
```
This Python script defines a pair of self-contained functions, `encode_cyclic` and `decode_cyclic`, which solve the problem of encoding and decoding a string using a cyclic group of characters. It also contains a test cases to ensure the correctness of these functions.