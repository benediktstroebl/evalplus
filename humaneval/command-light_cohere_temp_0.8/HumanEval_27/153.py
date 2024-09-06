```python
def flip_case(string: str) -> str:
    """
    Flip all characters in the given string, swapping lowercase to uppercase and vice versa.
    Returns the string with all characters flipped.
    """
Input is a string, and the output is also a string.
"""

    # Test case 1:
    test_string = "hello"
    flipped_str = flip_case(test_string)
    assert flipped_str == "hELLO"  # This is the expected output

    # Test case 2:
    test_string = "HELLO"
    flipped_str = flip_case(test_string)
    assert flipped_str == "hello"  # This is the expected output

    return flipped_str
```