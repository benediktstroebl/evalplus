```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0

    # Find the gcd using the built-in `math.gcd()` function
    took out the core library
    return math.gcd(a, b)

# Test cases
assert greatest_common_divisor(3, 5) == 1
assert greatest_common_divisor(25, 15) == 5
assert greatest_common_divisor(9, 6) == 3
assert greatest_common_divisor(54, 27) == 9
assert greatest_common_divisor(100, 50) == 50
assert greatest_common_divisor(181, 135) == 45
```
The code defines a function `greatest_common_divisor` that calculates the greatest common divisor of 2 integers `a` and `b`. It uses the built-in `math.gcd()` function from part of the core library. The `test cases` section contains some assertion checks to ensure the correctness of the function's implementation.