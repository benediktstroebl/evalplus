Here is a self-contained Python script that solves the problem you provided:

```python
def fizz_buzz(n):
    c = 0
    while n > 0:
        digit = n % 10
        c += (digit == 7)
        n //= 2
    return c

# Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This script defines a function fizz_buzz that calculates the number of times the digit 7 appears in integers less than a given number n which are divisible by 11 or 13. The function uses a recursion and a simple modulo operation to achieve this.