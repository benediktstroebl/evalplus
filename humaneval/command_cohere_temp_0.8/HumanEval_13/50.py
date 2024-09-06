```python
def greatest_common_divisor(a, b):
    """ Returns the greatest common divisor of two integers a and b """
    if a == 0:
        return b
    if b == 0:
        return a
    return greatest_common_divisor(b%a, a)
```

The GCD function uses Euclidean algorithm whereby the larger number's remainder at division is used to repeatedly divide the smaller number until that remainder is 1, at which point the divisor is the GCD of the two numbers. The base case of the recursion is when either number is 0, whereby the other number is then the GCD.