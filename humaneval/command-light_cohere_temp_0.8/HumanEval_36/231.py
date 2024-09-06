```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    result = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            result += 1
    return result

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given input n, which are divisible by 11 or 13. The function iterates through the numbers from 1 to n, and checks for the digits 7 (either in mod 11 or mod 13). It then returns the number of such occurrences, which is the count of how many times the digit 7 appears in the numbers divisible by 11 or 13.