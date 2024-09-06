```python
def fizz_buzz(n):
    return sum(n < c for c in range(1, n+1) if any(c % 11 == 7 or c % 13 == 7))

# Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(80) == 0
assert fizz_buzz(120) == 4

```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in a sequence of numbers less than `n`, which are divisible by 11 or 13. The function uses a array comprehension and the any() function to iterate through numbers from 1 to `n` and checks if any of the numbers are divisible by 11 or 13. The function then returns the expected number of occurrences of 7.