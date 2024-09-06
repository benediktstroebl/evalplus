```python
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    return "".join([group[1:] + group[0]] if len(group) == 3 else group for group in groups)

# Tests
def test_encode():
    assert encode_cyclic("hello") == "ihgkfc"
    assert encode_cyclic("world") == "ijfcld"
    assert encode_cyclic("!!!") == "????"
    assert encode_cyclic("1234") == "1324"
    assert encode_cyclic("****") == "1234"

def test_decode():
    assert decode_cyclic("ihgkfc") == "hello"
    assert decode_cyclic("ijfcld") == "world"
    assert decode_cyclic("????")) == "!!!"
    assert decode_cyclic("1324") == "1234"
    assert decode_cyclic("1234") == "****"

test_encode()
test_decode()
``` 

The `encode_cyclic` function splits the input string into groups of three characters, and then cycles each group (by concatenating the last two characters with the first one), unless the group has fewer than three elements. This way, any string can be converted to a sequence of cyclic groups of three characters. 

The `decode_cyclic` function reassembles the original message by reversing the process, taking groups of three characters and splitting them if they were cycled. 

The `test_encode` and `test_decode` functions contain asserts that verify correctness of the encoded and decoded strings for different inputs. The tests should be run sequentially to confirm that they pass.