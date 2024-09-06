```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(
        [
            group[1:] + group[0]
            for group in
            [(group[0], group[1], group[2]) for group in s.groups(3)
        if len(groups) < 3
        ]
    )

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
   
    test by passing the string encoded with encode_cyclic function
    """
    return s.replace("".3".

test_encode_cyclic = encode_cyclic.decode_cyclic
test_encode_cyclic = encode_cyclic.decode_cyclic()
print(test_encode_cyclic)
```
The given Python script defines a self-contained function called `encode_cyclic` and another function called `decode_cyclic`. The `encode_cyclic` function takes a string as input and returns an encoded version of the string. The function achieves this by cycling groups of three characters, and then returns the encoded string. The `decode_cyclic` function takes the input string as its argument and returns the decoded version of the string, which is the original text string. The functions are tested by passing the test string as an argument to both functions.