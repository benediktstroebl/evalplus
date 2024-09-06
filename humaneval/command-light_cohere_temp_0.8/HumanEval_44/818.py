```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number to another base
    """
    if x < 0 or base < 2:
        raise ValueError("Both number and base should be positive and greater than 1")

    if base == 10:
        return str(x)
    
    # Use str.format to add a format with base number
    result = []
    while x > 0:
        remainder = x % base
        result.append(chr(int('0' + remainder)))
        x //= base
        
    return ''.join(result)

def test_change_base():
    base = 10
    x = 8
    expected = '22'
    got = change_base(x, base)
    print(f"Got: {got}, Expected: {expected}")

test_change_base()
```
This code defines a function `change_base` that converts a given number `x` to a string representation using a specified base `base`. The test function `test_change_base` verifies this conversion by passing a test case with `base` set to 10 and `x` set to 8, and the expected output is `'22'`. The code also includes input validation to ensure that both the input number and base are positive and greater than 1. 
Finally, the output prints the results of the function to the console.