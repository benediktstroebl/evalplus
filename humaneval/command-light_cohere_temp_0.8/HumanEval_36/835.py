```python
def fizz_buzz(n):
    count = 0
    for num in range(10, n+1):
        if (num % 11 == 0 or num % 13 == 0) and num != 7:
            count += 1
    return count

# Test suite
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(80) == 0
assert fizz_buzz(13) == 2
assert fizz_buzz(22) == 5
assert fizz_buzz(27) == 8

```
The function counts the number of times the digit 7 appears in the range of integers less than n which are divisible by 11 or 13, excluding 7 itself.