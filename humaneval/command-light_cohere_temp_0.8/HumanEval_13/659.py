```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    
    # largest factor of a is the gcd of a and m
    if a > b:
        a, b = b, a
    
    # m is divisible by a, so take its gcd
    m = 0; i = 1
    while a % i == 0:
        m = i
        i += 1
    while a > 0 and m < b:
        a //= m
        m += 1
    return m

# test case 1
assert greatest_common_divisor(3, 5) == 1

# test case 2
assert greatest_common_divisor(25, 15) == 5

# test case 3
assert greatest_common_divisor(10, 5) == 5

# test case 4
assert greatest_common_divisor(27, 3) == 3
```
The function `greatest_common_divisor` calculates and returns the greatest common divisor of two given integers `a` and `b`. The function first checks if either number is `None`, and if so returns `0`. It then takes the smaller of the numbers as the dividend and makes `m` the divisor of `a` by iterating through the following:
- initializing `m` to 0 and `i` to 1. 
while `a % i == 0`:
 - if `a` is divisible by `i`, then `m` is set to `i`, and `i` is incremented by 1.
 - if `a` is greater than `0` and `m` is less than `b`, then `a` is divisible by `m`, so `a` is updated by `m` divided by `a` in each iteration. 
 loop exits when `a` becomes 0 or when `m` reaches `b`.