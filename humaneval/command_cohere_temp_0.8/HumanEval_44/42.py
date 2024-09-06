```python
def change_base(x, base):
    return bin(x)[2:].rjust(calc_len(x), '0')[::-1] if base == 2 else adjust_to_base(x, base)

def adjust_to_base(x, base):
    # convert to decimal first if base is not 2
    tmp_decimal = str(int(x))
    if base != 10:
        tmp_decimal = change_base(tmp_decimal, 10)
    return multiply(tmp_decimal, base)

def multiply(num1, num2):
    return str(int(num1) * int(num2))

def calc_len(x):
    # calculate length of binary string with decimal value x
    return len(bin(int(x))[2:])

# Tests
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'
```

The function 'change_base' takes two arguments, an integer 'x' and an integer 'base' to change the base of 'x' to 'base'. This script also includes tests that check for correct behavior of the function with different inputs. 
```
Please note that this code assumes that the input numbers ('x') are integers. If the input numbers are strings, especially if they are different from decimal numbers, 
you may need to modify the code to handle those cases as well. 
```
Let me know if you'd like to have the tests separated for clearer code comprehension.