```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    returns original string
    if "..." in s:
        return s.decode_cycl(s)
    elif "..." in s:
        return s.decode_cycl(s)
    else:
        return s

if __name__ == "__main__":
    s = "abc..."
    print("encode_cyclic:", encode_cyclic(s))
    print("decode_cyclic:", decode_cyclic(s))
```
This script defines two functions: `encode_cyclic` and `decode_cyclic`. The `encode_cyclic` function takes a string `s` as input and returns the encoded string by cycling groups of three characters. The `decode_cyclic` function takes a string `s` as input and returns the original string.

The script also includes a `main` block, which creates a string `s = "abc..."` and prints the results of calling the `encode_cyclic` and `decode_cyclic` functions with the string.

This code can be used to encode and decode markdown code blocks.