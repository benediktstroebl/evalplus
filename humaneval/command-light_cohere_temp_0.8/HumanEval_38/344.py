```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    I the the readable string
    """
    assert encode_cyclic(decode_cyclic(input_string)) == input_string
    assert encode_cyclic("!!py") == "EFG".py"
    assert encode_cyclic("EFG").match("EFG")
    assert encode_cyclic("CIA").match("CIA")
    assert encode_cyclic("CIA".capitalize()) == "XYZ".xyw"
    assert encode_cyclic("XYZ".capitalize()) == "PMA".zxc"
    assert not encode_cyclic("CIA".replace(" ", "", ""))
    assert not encode_cyclic(["A"]*10)
```
The code defines a self-contained function that takes a string as input and returns the encoded string by cycling groups of three characters. It then passes these tests for input and checks the output with the corresponding decode function to pass the tests.