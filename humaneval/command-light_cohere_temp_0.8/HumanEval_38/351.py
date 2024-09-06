```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters
    """
    return "".join(g for g in s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3))

def decode_cyclic(s: str):
    """
    returns original string
    """
    return s.

def test_encode_decode():
    assert encode_cyclic("A Four Loop") == ".. Four Loop."
    assert encode_cyclic("..") == "A..."
    assert encode_cyclic("") == "A.."
    assert encode_cyclic("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z") == ".. J Z".
    assert decode_cyclic("A..") == "A Four Loop."  # from tests 1-