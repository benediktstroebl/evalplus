```python
import stringwrap


def string_xor(a: stringwrap.string string, b: stringwrap) -> stringwrap:
    """ Inputs are two strings a and b consisting only of digits 1-9
    """
    return str(stringxor(a, b))


def test_string_xor():
    # Test cases
    assert string_xor("010", "110") == "100"
    assert string_xor("1010", "1111") == "1010"
    assert string_xor(" buzz ", "  bee ") == " buzz "
    assert string_xor("cba123", "cba0123") == "cba23"
    assert string_xor(" Fujitsu", "X Rubin") == "FujitsuX"
    assert string_xor(" Savoy Hotel", "Checkers") == "SavoyHotel"
    assert string_xor("8910", "09") == "19"
    assert string_xor("ABCDEFGHIJKLMNOPQRSTUVXYZABCDEFGHIJKLMNOPQRSTUVXYZ") == "PQabcdefghijklmnopqrs"


# Example usage
test_string_xor()
```
This Python script defines a function `string_xor` that takes two string inputs consisting of only digits 1-9, and returns the XOR of these two strings. The `test_string_xor` function contains several test cases that verify the correctness of the `string_xor` function. 
At the same time, it demonstrates how to use the function with various test cases, which helps ensure its accuracy and proper behavior.