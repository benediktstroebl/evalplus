```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient for larger integers as it constantly reduces the smaller of the two integers to recursion parameters. The base case of the recursion is b == 0, which returns a directly. Otherwise, the function returns the GCD of b and the remainder of a divided by b. Overall, this approach reduces the problem to finding the GCD of two smaller integers in each recursive call.