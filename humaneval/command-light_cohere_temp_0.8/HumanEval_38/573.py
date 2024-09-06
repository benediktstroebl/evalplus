```python
def encode_cyclic(s: str) -> str:
    """
    returns encoded string by cycling groups of three characters.
    # split string to groups Each of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    strategic decision for this fact.
    The following:
    - use spaces to implement readability and make the code look less convolicated.
    - use None for an better default value in case of an invalid string input.
    - use a string literals to make the function shorter and easier to read.
    """
    short_code:
    def cycle_encode(s: str) -> str:
        return f"{:.join(groups)}".format(groups=s.split(s, 3))
    def cycle_decode(s: str) -> str:
        return f"{:join(s)}".format(s)
```
This solution uses string formatting and a split/join technique, which I feel improves readability and avoids using lists. This strategy makes the both functions simple and user-friendly, which is the main goal of clean code.