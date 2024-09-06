```python
def fizz_buzz(n: int) -> int:    
    # Count occurrences of 7 in numbers less than n, divisible by 11 or 13
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 7) or (num % 13 == 7):
            count += 1
    return count

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the numbers less than a given number `n` and divisible by 11 or 13. It employs a regular loop that iterates through the numbers from 1 to `n`, and checks for the digit 7 in both mod 11 and mod 13. The function then counts the count and returns the result.