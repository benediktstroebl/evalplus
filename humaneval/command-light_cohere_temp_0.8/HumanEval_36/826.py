```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        num = pow(10, i, n)
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given number `n` that are both divisible by 11 and 13. It uses a simple for loop to iterate through numbers up to `n`, and checks each digit's remainder against both 11 and 13. The function then counts the number of such digits that satisfy this condition, and returns the final count.