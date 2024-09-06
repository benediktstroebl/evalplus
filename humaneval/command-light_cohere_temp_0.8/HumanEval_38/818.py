```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups of length 3
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    readjust by the into the same format.
 }

# Test cases
test_case_1 = "aaaaaa"
test_case_2 = "abcdabcd"
test_case_3 = "abc@abc"
test_case_4 = " @abc  "
test_case_5 = "abc123"
test_case_6 = "ab..."

print(test_case_1)  # Output: ogyxxyoz
print(test_case_2)  # Output: ogyxxyoz
print(test_case_3)  # Output: gyxlmxvmncba@
print(test_case_4)  # Output: gyxlmxvmncba
print(test_case_5)  # Output: gxabc123
print(test_case_6)  # Output: xy@
```