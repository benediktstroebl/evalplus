```python
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(1, n+1):
        num = str(i)
        is_divisible = (int(num[0]) % 2 == 0) or (num[1] == '7')
        if is_divisible:
            count += 1
    return count

# Test suite for function fizz_buzz
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(80) == 4
assert fizz_buzz(100) == 6
assert fizz_buzz(1000) == 8
```
The provided code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than a given number `n` that are divisible by 11 or 13. The function iterates through the numbers from 1 to `n` and checks if the first digit is divisible by 2 or if the last digit is 7. The function then counts how many of these numbers that meet these criteria and returns the result.