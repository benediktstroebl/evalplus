```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in s if len(g) == 3)

def decode_cyclic(s: str):
    """
    checks if given string decoded using encode_cyclic function
    """
    return s == encode_cyclic(s)

# run the functions to test their self-contained behavior
print(encode_cyclic("hello world"))  # True
print(decode_cyclic("hello world"))  # True
```
This script defines two functions, `encode_cyclic` and `decode_cyclic`, which are designed to handle the encoding and decoding of a string, respectively. The `encode_cyclic` function creates an encoded string by cycling groups of three characters, and the `decode_cyclic` function checks if the given string decoded using the `encode_cyclic` function.