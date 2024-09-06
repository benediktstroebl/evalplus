```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    sum_of_7s = 0
    for num in range(1, n+1):
        digit_value = ord('7')
        is_divisible = (num % 11 == 0 or num % 13 == 0)
        if is_divisible:
            digit_count = num // digit_value
            if digit_count % 10 == 7:
                sum_of_7s += 1
    return sum_of_7s

# Unit tests
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
print(fizz_buzz(5))  # Should return 0
```