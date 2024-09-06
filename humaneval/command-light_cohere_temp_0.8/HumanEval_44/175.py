```python
def change_base(x: int, base: int):
    if isinstance(x, str):
        return x.
    elif base < 0 or
            else:
        raise ValueError("Invalid base number")
    return '{0}'.format(x, base)

def test_change_base():
    try:
        x = 8
        base = 3
        result = change_base(x, base)
        assert isinstance(result, str) and result == '22', result
        assert result == change_base(x, 5)
        assert result == change_base(x, 2)
        assert result == change_base(x, 13)
        assert result == change_base(x, 10)
        assert result == change_base(x, 17)
        assert result == change_base(x, 41)
        assert result == change_base(x, 7)
        assert result == change_base(x, 97)
    except ValueError as e:
        print("Error:", str(e))

# Run the test function
test_change_base()
``` 
The function change_base takes an integer x and a base number base as input and converts the x to a string using the specified base. The base numbers can be 0 (decimal), 10 (decimal, integer), or any other custom base. The function uses the string representation of x, then performs the conversion using the `format()` method, which returns the corresponding string representation. The test_change_base function attempts to validate the function by passing different inputs and checking the resulting string representations against the expected output. The test function uses the string representation of the base and performs the conversion using the `format()` method with a base of 0. The resulting string should match the expected output.