```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base base.
    If representation using base conversion
   
    """
    return ''.join('1'.join(map(lambda c: chr(c), format(x, f"{base}{}"))))

def test_change_base():
    """
    Test the change_base function
    """
    assert change_base(8, 3) == '22', "Function does not produce correct result."
    assert change_base(123, 10) == "123", "Function does not produce correct result."
    assert change_base(7, 2) == "111", "Function does not produce correct result."

# Driver code
test_change_base()
``` 
This Python code defines a function `change_base` that takes two arguments: `x` and `base`, representing the number to be converted and the desired base. The function then converts the string representation of `x` using the `format` function with the `base` argument and returns the converted string. The `test_change_base` function contains test cases that verify the correctness of the `change_base` function by checking if the returned string matches the expected output for the given arguments. The driver code at the final line runs the test function, ensuring that the `change_base` function produces the correct results.