```python
def change_base(x, base):
    return bin(x)[2:].rjust(calc_len(x), '0')[::-1] if base == 2 else adjust_to_base(x, base)


def adjust_to_base(x, base):
    digits = '0123456789ABCDEF'
    ret = []
    while x > 0:
        x, r = divmod(x, base)
        ret.append(digits[r])
    return ''.join(ret)[::-1]


def calc_len(x):
    base = 2
    while x > 1:
        x //= base
        base //= 2
    return len(bin(base)[2:])

# Tests
assert change_base(8, 3) == '22'
assert change_base(8, 2) == '1000'
assert change_base(7, 2) == '111'
```

The function `adjust_to_base` is used to handle bases other than 2, it converts the digits of the number to the specified base and reverses the result. The `calc_len` function calculates the length of the result string in binary by iteratively dividing the number by 2 until it's 1, capturing the number of digits required to represent the number in binary. The main `change_base` function first checks if the base is 2, in which case it directly uses the built-in `bin` function to convert the number to a binary string; otherwise, it calls the adjusted converter function.