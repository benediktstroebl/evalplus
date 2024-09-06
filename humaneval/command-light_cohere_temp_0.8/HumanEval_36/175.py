```python
def fizz_buzz(n: int):
    total = 0
    for num in range(2, n+1):
        count = 0
        for i in range(10):
            if num % i == 0 and i <= 7:
                count += 1
        if count == 2:
            total += 1
    return total

# Test case to check the function
print(fizz_buzz(50))
print(fizz_buzz(78))
print(fizz_buzz(79))
```

This Python function, `fizz_buzz`, calculates the number of occurrences of the digit 7 in numbers that are less than a given number `n` and are divisible by 11 or 13. It iterates through numbers from 2 to `n` and checks if the number is divisible by any number from 1 to 9 using a `counting` loop. The function then adds 1 to the total count if the condition is met.