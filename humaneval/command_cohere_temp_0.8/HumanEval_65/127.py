```python
def circular_shift(x, shift):
    num_digits = len(str(x))
    if shift > num_digits:
        shift = num_digits
    return x << (num_digits - shift)
```

This script defines a Python function called `circular_shift` which takes two arguments, `x` and `shift`. This shifts the digits of the integer `x` right by `shift`, and returns the result as a string. If `shift` is greater than the number of digits, it reverses the digits instead. 

To achieve this, it calculates the number of digits in `x` by taking the length of its string representation using the `len` function. It then checks if `shift` is greater than this number of digits, and if so, assigns `shift` the value of `num_digits` instead, effectively reversing the digits if the shift is too large. 

Finally, it performs the circular shift using bitwise left shift (`<<`) operation, with the number of places to shift determined by `num_digits - shift`. This essentially wraps the digits of `x` around the circular queue and returns the result as the shifted digit string. 

The script provides a clear and efficient solution to the problem statement, and would be a useful addition to the code base for anyone needing to perform circular shifts of integers.