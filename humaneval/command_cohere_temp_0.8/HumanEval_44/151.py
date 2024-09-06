```python
def change_base(x, base):
    return bin(x)[2:].rjust(calc_len(x), '0')[::-1] if base == 2 else adjust_to_base(x, base)


def adjust_to_base(x, base):
    digits = '0123456789ABCDEF'
    conversion = []
    while x > 0:
        x, r = divmod(x, base)
        conversion.append(digits[r])
    return ''.join(reversed(conversion))


def calc_len(x):
    base = 2
    while x > 1:
        x //= base
        base //= 2
    return max(base, x + 1)

# Tests
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'
```

The function `change_base` takes two arguments: `x`, the number to be converted, and `base`, the target base. 

It uses the built-in `bin` function to convert the number `x` to a binary string and then removes the leading '0b' to adapt it to a string representation in the desired base. To handle bases other than 2, it falls back to the `adjust_to_base` function. This function performs a digit-by-digit conversion of `x` to the target base, using `divmod` to extract each digit and convert it accordingly. The `calc_len` function calculates the length of the resulting string, ensuring it has enough leading zeros to pad it properly.

The tests assert the correct behavior of the function for the given inputs. Please note that the code assumes that the numbers provided as input are valid, and it may yield unexpected results for invalid numbers. Adjustments could be made to handle edge cases and invalid inputs.