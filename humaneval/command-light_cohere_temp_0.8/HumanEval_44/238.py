```python
def change_base(x: int, base: int):
    """
    Change the base of a number x to the desired base.

    Args:
        x: int, number to be converted
        base: int, base to which the number is converted

    Returns:
        str: string representation of the number after base change
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    # convert number to string with desired base
    base_str = str(x)
    if base == 10:
        base_str = base_str.replace(x=(-int(base_str),len(base_str), '0'))
    return base_str

def test_change_base():
    """Unit tests for change_base function"""
    base_list = [10, 11, 12, 20, 21, 22, 23, 24, 25, 30, 31, 32, 33, 34, 35]
    base_map = {i: str(i) for i in base_list}
    x_list = [base_map[i] for i in base_list]
    for x, base in zip(x_list, base_list):
        result = change_base(x, base)
        assert result == base
        print(f"test passed: {x} ({base}) became {result}")

if __name__ == "__main__":
    test_change_base()
``` 
This script defines the function `change_base` that converts a given number `x` to a string representation with the desired base `base`. The function also includes a set of unit tests using the `test_change_base` function to verify its correctness.