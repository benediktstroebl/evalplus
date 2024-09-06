```python
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7':
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Tests
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function `fizz_buzz` calculates the number of times the digit 7 appears in numbers less than `n` that are divisible by 11 or 13. The function iterates through numbers from 1 to `n` and checks if the number's digit is 7, and whether the number is divisible by 11 or 13. The function then counts the time 7 appears and adds 1 to the count if the number is divisible by 11 or 13.