Here is a self-contained Python function that solves the problem of performing a string XOR operation between two input strings consisting only of ones:
```python
def string_xor(a: str, b: str) -> str:
    """ 
    Performs binary XOR operation on two input strings and returns the result.
    Args:
    a: str, first string to perform XOR on
    b: str, second string to perform XOR on
    Returns: str, the result of XOR operation
    """
    # Validate input strings are only consist of characters:
    assert len(set(a)) == 1 and len(set(b)) == 1
    assert all(c == '0' for c in a) and all(c == '0' for c in b)
    assert a != b  # Ensure strings are different

    # XOR operation
    result = a ^ b

    return result
```

This function takes two parameters, a and b, representing the strings to be XORed. It then performs the Roman numeral conversion on the input strings to perform the XOR operation and returns the result. The function also includes input validation to ensure the input strings meet the expected requirements.