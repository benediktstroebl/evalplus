Here is a self-contained Python function that solves the problem you described:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    opened with brackets and closed with space
    """
    return " ".join(s.split(" " ")[::-1])

# Test cases
test_cases = [
    "abc..",
    "..abc",
    " ........",
    "abc...",
    " .",
    "a ab   ",
    "a aa  b"
]

for t in test_cases:
    print(t, end=" ")

# Function Calls
print(encode_cyclic(t))
print(decode_cyclic(t))
```

This script defines a function called `encode_cyclic` that converts a string into an encoded format. It then defines a `decode_cyclic` to decode this encoded format back into a string. The script also defines some test cases to test the function, and the function is then called with each test case.