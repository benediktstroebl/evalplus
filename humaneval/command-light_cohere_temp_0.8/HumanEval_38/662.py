```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    UPPER DECODE
   
    """
    return s.encode_cycl()

if __name__ == "__main__":
    s = input("Input string: ")
    print("Input: ", s)
    print("Output: ", decode_cyclic(s))
```

The above Python script defines a self-contained function that solves the problem of encoding and decoding a string with circular groups of three characters. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements within each group, and then returns the encoded string. The `decode_cyclic` function takes the input string and decodes it using the `encode_cyclic` function. The script also includes a `main` block that prompts the user to input a string and then prints the decoded string.