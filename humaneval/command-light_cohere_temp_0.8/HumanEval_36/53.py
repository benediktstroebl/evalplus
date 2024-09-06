```python
def fizz_buzz(n):
    return (n < 10 and len([x for x in str(n) if x == 7]) == 0) or \
           (n >= 10 and len([x for x in str(n) if x == 7]) == 1 and n % 10 == 7) or \
           (n >= 10 and len([x for x in str(n) if x == 7]) == 2 and n % 13 == 7)

# Unit tests
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(100) == 4
assert fizz_buzz(9) == 0
assert fizz_buzz(13) == 4
assert fizz_buzz(0) == 0
assert fizz_buzz(2) == 1
```

This Python script defines a function called fizz_buzz, which returns true or false based on the number n. The function uses a different criteria to determine whether the number contains the digit 7. The unit tests are also provided to ensure that the function works as expected.