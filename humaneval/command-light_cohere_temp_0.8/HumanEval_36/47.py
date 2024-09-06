```python
def fizz_buzz(n):
    if n <= 0:
        return 0
    count = 0
    while n % 10 != 7:
        n //= 11
    count += 1
    return count

#Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(80) == 4
assert fizz_buzz(120) == 6
assert fizz_buzz(156) == 7
assert fizz_buzz(777) == 8
```