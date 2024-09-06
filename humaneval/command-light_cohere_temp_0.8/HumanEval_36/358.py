```python
def fizz_buzz(n: int):
    count = 0
    for num in range(2, n+1):
        num = str(num)
        if num[-1] == "7":  # Check if last digit is 7
            count += 1
        if num % 11 == 0 or num % 13 == 0:  # Check if number is divisible by 11 or 13
            count += 1
    return count
```