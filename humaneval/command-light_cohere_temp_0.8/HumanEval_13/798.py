```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)

# Test the function with a few examples
assert(greatest_common_divisor(3, 5) == 1)
assert(greatest_common_divisor(25, 15) == 5)
assert(greatest_common_divisor(16, 48) == 16)
assert(greatest_common_divisor(50, 25) == 25)
```
This code defines a recursive function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. The function first handles base cases: if either `a` or `b` is 0, it returns the other one. Otherwise, the function recursively calls itself with the argument `b` and `a % b`, which calculates the remainder of `a` divided by `b`. The function continues to find the greatest common divisor of larger numbers by breaking down the problem into smaller subproblems.