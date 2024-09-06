```python
def change_base(x: int, base: int):
    """
    Change the base of a number to another base.
    :param x: int (number to be converted)
    :param base: int (base to convert to)
    :return: string
    """
    if x < 0 or base < 2:
        raise ValueError("Invalid input values.")
    return format(x, base)

# Testing function
def test_change_base():
    try:
        x = 8
        base = 3
        result = change_base(x, base)
        assert result == '22'  # Should be '22'
        x = 8
        base = 2
        result = change_base(x, base)
        assert result == '1000'  # Should be '1000'
        x = 7
        base = 2
        result = change_base(x, base)
        assert result == '111'  # Should be '111'
    except ValueError as e:
        print(f"Error: {e}")

# Run the tests
test_change_base()
``` 
This code defines the `change_base` function that converts a number to a new base. It uses the format function to accomplish the conversion. The function includes input validation to ensure that base values are valid. The test function is used to check that the `change_base` function behaves correctly.