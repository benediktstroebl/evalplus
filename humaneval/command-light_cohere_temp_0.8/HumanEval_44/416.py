```python
def change_base(x: int, base: int):
    """
    Change the base of a number to a specified base.

    Args:
        x: int, number to be converted
        base: int, base to which the number will be converted

    Returns:
        string representation of x in the specified base
    """
    return str(x, base)

def test_change_base():
    base = 10
    x = 8
    expected = '22'
    actual = change_base(x, base)
    assert actual == expected, f"Expected {expected}, got {actual}"

if __name__ == "__main__":
    test_change_base()
```
The above code defines a function change_base which converts a number to a specified base. The function takes two arguments: the number to be converted (x) and the base to which the number will be converted (base). The function then returns the string representation of the number in the specified base.

The test_change_base function is used to test the functionality of the change_base function. The function sets a base and a number x, then calls the change_base function with those arguments and compares the actual output with the expected output. Finally, it asserts that the actual output matches the expected output.

This code is self-contained and provides a solution to the problem of changing the base of a number to a specified base.