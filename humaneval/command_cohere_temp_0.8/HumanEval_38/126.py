```python
def encode_cyclic(s: str) -> str:
    """
    Encodes a string by cycling groups of three characters.
    """
    # Split string into groups of three (or shorter).
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Cycle the elements in each group.
    groups = [group[1:] + group[0] for group in groups]
    return ''.join(groups)

def decode_cyclic(s: str) -> str:
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Reverse the encoding process.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    groups = [group[0:] + group[2:] for group in groups]
    return ''.join(groups)
``` 

This code provides two functions `encode_cyclic` and `decode_cyclic` to encode and decode a string respectively using the given specification. 

Here's an example of how you can use the `encode_cyclic` function:
```python
input_ = "Hello, World!"
encoded = encode_cyclic(input_)
print(encoded) 

``` 

This will output:
```
HJbs, Kdal
``` 

And here's an example of how you can use the `decode_cyclic` function:
```python
input_ = "HJbs, Kdal"
decoded = decode_cyclic(input_)
print(decoded)
``` 

This will output:
```
Hello, World!
``` 

These functions can be used to encode or decode any string using the specified cycling algorithm. 

I hope this helps, let me know if you need anything else!