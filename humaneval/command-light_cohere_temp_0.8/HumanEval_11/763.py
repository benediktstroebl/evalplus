```python
import stringprep

def string_xor(a: str, b: str) -> str:
    """ Function performs XOR of two input strings containing only digits
    """
    assert len(set(a)) == len(set(b)), "Input strings must have equal length"
    assert set(a) & set("0123456789") == set("0123456789"), "Input contains invalid character"
    assert len(set(str(a) + str(b))) == len("01"), "Input strings contain extra 0s"
    return str(a ^ b)

test_string_xor = stringprep.test_string_xor()
```