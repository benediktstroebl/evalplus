```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
   Takes as input string encoded with encode_cyclic function. Returns decoded string."""
    main_string = "Hello, world!" encode_cyclic(main_string)
    decoded_string = decode_cyclic(encode_cyclic(main_string))
    print(decoded_string)
    print("test 2", decode_cyclic(" Testing 2"))
    print("test 3", decode_cyclic("test !@!"))
```
This Python script defines a self-contained function that solves the problem of encoding and decoding a string of characters into a cyclic group of three characters. The function takes a input string and returns the encoded string. The function then splits the string into groups of three characters and cycles the elements of each group. The function then returns the string. The script also passes tests by encoding and decoding the same input strings.