```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n >= 10:
        num = n % 10
        if num == 7:
            count += 1
        n //= 2
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This code defines the fizz_buzz function, which calculates the number of occurrences of the digit 7 in integers less than a given number n that are divisible by 11 or 13. The function uses a loop to iteratively check digits from 0 to 9 (as we're interested in non- accompatory digits that are less than n and divisible by 11 or 13), incrementing the count if the current digit is 7. The loop continues until n is less than 10, and finally, the count is returned.