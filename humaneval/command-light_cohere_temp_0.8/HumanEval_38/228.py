```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g) for g in encode_cyclic_groups(s))

def encode_cyclic_groups(s: str):
    """
    splits string to groups of length 3
    """
    return [(g[1:] + g[0]) if len(g) == 3 else g for g in s.format = ''.join(
        s.split('').split('').split(''))[::3::])
    ```

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
```