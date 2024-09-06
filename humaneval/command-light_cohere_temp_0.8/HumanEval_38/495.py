```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g[1:] + g[0])  # using list comprehension to join

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    important decoded string, it uses the encode_cyclic function

test_encode_decode = ["hello", "world", "abc", "123", "abcabc"]

print(test_encode_decode == encode_cyclic(test_encode_decode))
print(decode_cyclic(test_encode_decode) == test_encode_decode)
```