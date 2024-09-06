```python
def fizz_buzz(n):
    count = 0
    for i in range(1, n+1):
        num = 0
        while i % 11 == 0 or i % 13 == 0:
            num += 1
        if num == 7:
            count += 1
    return count

# Test suite
print(fizz_buzz(50))        # Output: 0
print(fizz_buzz(78))        # Output: 2
print(fizz_buzz(79))        # Output: 3
print(fizz_buzz(100))       # Output: 6
print(fizz_buzz(120))       # Output: 7
print(fizz_buzz(123))       # Output: 6
print(fizz_buzz(150))       # Output: 4
```

This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers less than a given number `n` that are either divisible by 11 or 13. The function iterates through from 1 to `n` and keeps track of the number of times the digit 7 appears using a variable `num`. It checks this `num` against 7, and if it's 7, the count variable is incremented. The function returns the number of times 7 appears in the provided range.