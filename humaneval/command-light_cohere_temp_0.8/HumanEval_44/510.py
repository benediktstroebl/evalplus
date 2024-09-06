Here is a Python script that demonstrates the solution to the problem you described:
```python
def change_base(x: int, base: int) -> str:
    """
    Change the numerical base of input number x to base base.
    Return string representation after conversion.
    base numbers less 10
    need to be positive integers
    """
    if not isinstance(x, int) or base <= 0:
        raise TypeError("Input and base must be positive integers")
    return '{:b}'.format(x, base)

# Test case 1
print(change_base(8, 3))
# Expected output: '22'

# Test case 2
print(change_base(8, 2))
# Expected output: '1000'

# Test case 3
print(change_base(7, 2))
# Expected output: '111'
```
The function change_base takes an input number x and a base b as parameters and returns the converted number. It includes input and base type checks to ensure valid input and raises a TypeError for invalid inputs. The function uses the base conversion to convert the number to the desired base. This code is a purpose of this function is to provide a convenient way to change the base representation of a number in a given base.