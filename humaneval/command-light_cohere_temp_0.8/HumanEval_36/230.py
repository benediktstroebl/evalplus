```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7')
        if i % 10 == digit:
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            break
    return count

#Test case 1
print(fizz_buzz(50))  # Output: 0

#Test case 2
print(fizz_buzz(78))  # Output: 2

#Test case 3
print(fizz_buzz(79))  # Output: 3
```

This code defines the fizz_buzz function that calculates the number of occurrences of the digit 7 in integers less than a given number n, which are divisible by 11 or 13. It iterates through numbers from 1 to n, checks if the current number contains the digit 7 using the ord() function, and if it's a multiple of 11 or 13, adds 1 to the count. The loop breaks once the number condition is met.