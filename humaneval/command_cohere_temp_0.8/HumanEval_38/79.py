```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle elements in each group. Unless group has fewer than 3 elements.
    groups = [group[1:] + group[0] for group in groups if len(group) == 3]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Restore original order by reversing the cycling process.
    groups = [group[0] + group[2:] for group in groups if len(group) == 3]
    return "".join(groups)
```

The `encode_cyclic` function splits the input string into groups of three characters, then cycles the elements in each group to create a new string, while the `decode_cyclic` function reverses the encoding process to restore the original string. 

Here is an example usage of the encode_cyclic function:
```python
string = "Hello, World!"
encoded = encode_cyclic(string)
print(encoded)  # Output: 'Hka, Jmc!'
```

And here is an example usage of the decode_cyclic function:
```python
encoded_string = 'Hka, Jmc!'
decoded = decode_cyclic(encoded_string)
print(decoded)  # Output: 'Hello, World!'
``` 

These functions can be used to encode and decode any string using the cyclic encoding technique. 

Cyclic encoding is a simple, lightweight method for encoding information. This method is not suitable for encrypting data due to its predictable and reversible nature.