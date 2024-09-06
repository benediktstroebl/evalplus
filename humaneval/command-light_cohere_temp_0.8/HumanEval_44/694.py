```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of a number to the desired base.
    Args:
        x: int or string representing a number to be converted
        base: int, base of the number system
    Returns:
        string representation of the converted number
    """
    if isinstance(x, str):
        # handle string input
        x = int(x)

    if base < 2 or base > 36:
        raise ValueError("Invalid base value. Please use numbers from 2 to 36")

    # convert number to base 10 and return string representation
    return format(x, "{:b}", base)

# test the function with input arguments int and int
test_change_base(42, 10) # 42 -> 4200
test_change_base("hello", 2) # hello -> 'hhello'
test_change_base(123, 3) # 123 -> '123'
test_change_base(1231, 4) # 1231 -> '21231'
```  The provided code defines a function change_base that converts a number to a different base. It takes two basic inputs: a base value and a number to be converted. The function handles string inputs by converting them to integers using the int() function. It ensures that the base value is within the valid range (2 to 36) by raising a ValueError exception if the base is not valid. The function converts the number to base 10 and returns the string representation using the format() function with the desired base. This code demonstrates the format and is widely used for converting numbers.