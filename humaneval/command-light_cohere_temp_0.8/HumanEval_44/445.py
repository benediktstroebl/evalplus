```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base.

    Args:
        x: int or string, number to be converted
        base: int, base to which the number will be converted

    Returns:
        string representation of the number, converted to the new base
    """
    if isinstance(x, str):
        x = int(x)

    if base <= 0 or base > 36:
        raise ValueError("Invalid base value")

    ret = []
    while x >= 10:
        ret.append(str(int(x // 10, base)))
        x = x % 10
    if x != 0:
        ret.append(str(x))

    return ''.join(''.join(ret, base))

# Unit tests
def test_change_base():
    assert change_base(7, 2) == '111'
    assert change_base('8', 3) == '22'
    assert change_base(10, 10) == '1'
    assert change_base('A', 2) == 'A'
    assert change_base(3, 12) == '111'
    assert change_base(10, 32) == '00000000000000010'
    assert change_base('abc123', 15) == 'zabc123z'

if __name__ == "__main__":
    test_change_base()
 ``` 
This Python code defines the change_base function, which converts a number to a new base. It handles cases where the supports both positive integers and strings. The function performs the conversion iteratively using a loop and applies the conversion rule "each digit of base 10 is added to the original number".