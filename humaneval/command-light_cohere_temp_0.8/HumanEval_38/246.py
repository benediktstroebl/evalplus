```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters
    s = input()
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    read from a source code that uses the encode_cyclic function. 
    """
   
    tests:
    """
    assert encode_cyclic("grouoogeroog r") == "ugroogGROOGR"
    assert encode_cyclic("grough") == "roughUOG"
    assert encode_cyclic("") == ""
    assert encode_cyclic("g g r o o g r oog") == "ugroogGROOGR"
    assert encode_cyclic("kayopaay oay") == "kgohyORAY"
    assert encode_cyclic("aa") == "aaga"
    assert encode_cyclic("") == ""
    assert encode_cyclic("aaaa") == "aaaaaaga"
```
The provided code defines two functions, `encode_cyclic` and `decode_cyclic`, that perform cyclic encoding and decoding on a given input string. 

The `encode_cyclic` function splits the input string into groups of three characters and then cycles the elements within each group. It uses a groups are formed by taking the first character from each group, then appending it to the last character in the group, if the group has exactly three characters. If the group has fewer characters than three, it simply returns the group as it is. The `decode_cyclic` function takes an encoded string as input and returns the decoded string. It uses the same to compare the decoded string with the original input string and pass all tests.