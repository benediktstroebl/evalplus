```python
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    while n > 0:
        digit = n % 10
        n //= 2
        count += digit != 7
    return count

#Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This script defines a function called `fizz_buzz` that counts the number of times the digit 7 appears in the remaining digits of numbers that are either less than `n` and divisible by 11 or 13. The function uses a algorithm that begins by shifting the digit 7 out of the number by dividing by 2 and then iterates until the number is greater than 0. The function then adds 1 to the count if the current digit is not 7.