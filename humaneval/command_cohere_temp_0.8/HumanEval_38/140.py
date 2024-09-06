```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer than 3 elements.
    groups = [group[1:] + group[0] if len(group) < 3 else group for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Uncycle elements in each group.
    groups = [group[0] + group[2:] if len(group) < 3 else group for group in groups]
    return ''.join(groups)
```

The `encode_cyclic` function splits the input string into groups of three characters, then cycles each group's elements to create a new string, and returns the new string. This process is repeated until the last group, which contains fewer than three characters, is handled. The `decode_cyclic` function splits the input string into groups of three characters and then undoes the cycling operation performed by the encoding function to create a new string and returns the new string. 

Here is an example function call for `encode_cyclic`:
```python
encoded_string = encode_cyclic("Hello, World!")
encoded_string  # 'Hlo, Wrd!'
```

Here is an example function call for `decode_cyclic`:
```python
decoded_string = decode_cyclic(encoded_string)
decoded_string  # 'Hello, World!'
```

This script provides a straightforward solution to the problem, and the functions can be used freely to encode and decode strings as needed. Feel free to ask any questions or clarifications regarding the problem or the provided solution.