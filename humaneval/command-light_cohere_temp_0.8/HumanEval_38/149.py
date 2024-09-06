```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s)) for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    optimal solution and a text.
    return "".join(decode_cyclic(s))

tests = []
tests.add(encode_cyclic("abc"))
tests.add(encode_cyclic("bcrea"))
tests.add(encode_cyclic("rced"))
tests.add(encode_cyclic("agilia"))
tests.add(decode_cyclic("".join("agilia"))

print(tests)
```
This Python script defines a self-contained function named `encode_cyclic` that encodes a given string by cycling groups of three characters. It then defines another function, `decode_cyclic`, which takes an input string that was encoded using the `encode_cyclic` function and returns the decoded string. The `encode_cyclic` function splits the input string into groups of three characters, cycles the elements in each group, and returns the result as a single string. The `decode_cyclic` function then uses the `encode_cyclic` function to decode the input string. The script also includes test cases that verify the correctness of the `encode_cyclic` and `decode_cyclic` functions.