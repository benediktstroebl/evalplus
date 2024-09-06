```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups Each of length 3.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    # cycle elements in each group
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)

def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string
    UTC

    # test case 1: test string with 4 groups
    assert encode_cyclic("ABCDEFGHIJKLMNOPQRSTUV") == "..DEFG...IP..OM...RS...TV..."

    # test case 2: test string with 2 groups
    assert encode_cyclic("ABCEGH") == "..."

    # test case 3: test string with 3 groups
    assert encode_cyclic("ABCDEFGHIJKLMNOP") == "..DEFG..IP..O..."

    # test case 4: test string with 2 different characters
    assert encode_cyclic("ABC") == "..."

    # test case 5: test empty string
    assert encode_cyclic("") == ""

    # test case 6: test with spaces
    assert encode_cyclic("   ABC  ") == "   ..DEFG   ..I..."

    # test case 7: test with special characters
    assert encode_cyclic("ABC#$%&") == "..."

    # test case 8: test with different lengths in groups
    assert encode_cyclic("ABCDEFGHIJKLMNOPQRSZYXWVUTSRQPONMLKJ") == "..DEFG...@..OM...@..RP.."

    return "Passed all tests"
 ```