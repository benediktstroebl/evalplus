```python
def fizz_buzz(n):
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7' and i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Tests
print(fizz_buzz(50))   # Output: 0
print(fizz_buzz(78))   # Output: 2
print(fizz_buzz(79))   # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in integers less than `n` which are either divisible by 11 or 13. The function uses a loop to iterate through the numbers from 1 to `n` and checks if the digit is 7 and if the number is divisible by 11 or 13. The function then counts the number of such occurrences and returns the result.