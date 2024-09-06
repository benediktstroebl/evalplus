```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in s. groups]
    string = "".join(groups)
    return string

def decode_cyclic(s: str):
    """
    returns decoded string by using encode_cyclic function
    return encode_cyclic(s)[::-1]

# Example 1: Encode and Decode
print(encode_cyclic("Hello world."))  # Output: B Emanuellloh
print(decode_cyclic("B Emanuellloh"))  # Output: Hello world

# Example 2: Decode Only
print(decode_cyclic("B Emanuellloh"))  # Output: Hello

# Example 3: Encode String with Only Two Characters
print(encode_cyclic("Hello"))  # Output: BL
print(decode_cyclic("BL"))  # Error: cannot decode to string of length 1)

# Example 4: Encode String with More Than Three Characters
print(encode_cyclic("world"))  # Output: B w olldrld

```
This script defines two functions: `encode_cyclic` and `decode_cyclic`, which are used to encode and decode a string by grouping it into cycles of three characters. It then provides a corresponding test cases to demonstrate the functionality.