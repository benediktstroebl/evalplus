```python
def change_base(x: int, base: int):
    """
    Change the base of input number x to base b.
    :return string representation of the
    : return the base converted number
    """
    if x < 0:
        raise ValueError("Input number should be non-negative")
    return '{:0b}'.format(x, base)

def test_change_base():
    try:
        eight = int('8')
        result = change_base(8, 2)
        print(result)
    except ValueError as e:
        print("Error:", str(e))
    return True

test_change_base()
 ``` 
This script defines a function `change_base` that takes an integer `x` and an integer `base` as input. The function then performs the process of converting the base of the input number `x` to the specified base `base`. The function returns the base-converted string representation of the number. 
The `test_change_base` function attempts to call `change_base` with a test value and checks for exceptions. If no exception is thrown, the function prints the result and returns `True`.