Here's the Python script that includes the self-contained function with the given docstrings and tests:
```python
def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    groups = s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)
    return "".join(groups)

def decode_cyclic(s: str):
    """
    returns decoded string from encode_cyclic function.
    return s.encode_cycl
 plain text.
    """

def test_encode_decode():
    # Test case 1
    test_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZBC"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$GR$@Z$^LM$+@I$UD$@F$@J@H@K$@G$"

    # Test case 2
    test_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$@ABC$@DEF$@GHIJKLM@NOPQR$@STUVWXYZ"

    # Test case 3
    test_str = "abcdefghijklmnopqrstuvwxyz"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$@M$@@Z$@@@@@@H$@K$@@L$@G$@@@@@@"

    # Test case 4
    test_str = "abcdefghijklmnopqr#uvwxyz"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$@#@AB$@@@@@@@F$@G@@@@@@"

    # Test case 5
    test_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZBC"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$@Z$@@@G$@@@@@@H@@K$@@F@@@"

    # Test case 6
    test_str = "abcdefghijklmnopqrwxyz"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$@@@A$@@@@@@@@@G$@@@@@@@@@"

    # Test case 7
    test_str = "abcdefghijklmnopwsz"
    result = encode_cyclic(test_str)
    print(f"Original: {test_str}")
    print(f"Encoded: {result}")

    assert result == ".$@@@@F@@@@@@@@G$@@@@@@@@Z"

    # Test case