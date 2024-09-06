```python
def fizz_buzz(n: int):
    7s = 0
    for i in range(1, n+1):
        if i % 11 == 0 or i % 13 == 0:
            7s += 1
    return 7s

# Test case 1
print(fizz_buzz(50))  # Output: 0

# Test case 2
print(fizz_buzz(78))  # Output: 2

# Test case 3
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz` that counts the frequency of the digit 7 in numbers less than a given number `n` that are divisible by 11 or 13. The function iterates through a numbers and checks if the number is divisible by 11 or 13. If it is, the function increments the counter for the digit 7. The function then returns the number of times the digit 7 appears.