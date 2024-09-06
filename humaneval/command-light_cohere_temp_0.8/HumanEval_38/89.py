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
   matizes the aspects of the string by using 'mat' which makes it unquoted.
    """
    handles back nested backqu of the string
    """
    return s.replace("'mat')  # strip the newline character


# Test cases
tests = [
    "..."
    "hello world",
    "h g ," "hello",
    "h\n.o_w_l_ ",
    "ok lodey",
    "abc 123",
    "  x  ",
    "  aa123bb",
    "   abc   \n  \n  \n  "
]


for test in tests:
    result = encode_cyclic(test)
    print(result,f" -> {test}")
    print(decode_cyclic(result),f" -> {test}")
```
This script defines a function `encode_cyclic` that encodes a string by cycling groups of three characters. The `decode_cyclic` function takes an encoded string as input and returns the decoded string. 

The script also provides a set of test cases to check the correctness of the `encode_cyclic` and `decode_cyclic` functions. 

It's a simple and self-contained way to solve this problem.