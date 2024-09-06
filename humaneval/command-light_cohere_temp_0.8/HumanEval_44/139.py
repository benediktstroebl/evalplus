```python
def change_base(x: int, base: int):
    """
    Change the base of the input number x to the specified base.
    :return string representation after conversion
    """
    if x < 0:
        raise ValueError("Input number cannot be negative")
    return format(x, base)

def test_change_base():
    try:
        base = 10
        x = 8
        result = change_base(x, base)
        print(f'Result: {result}')
    except ValueError as e:
        print(f'Error: {e}')
    return result == '22'

# Execute the test function
test_change_base()
 ``` 
This Python script defines the function `change_base`, which converts a given number x to a specified base. The function raises a error if x is negative, and it returns the formatted number with the specified base using the `format` function. 
The test_change_base function tests this function by passing a base of 10 and an input number 8.  It also tests whether the result is '22' or not.