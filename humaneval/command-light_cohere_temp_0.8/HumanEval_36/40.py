```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for num in range(1, n+1):
        digit = str(num)[-n]
        if digit == '7':
            count += 1
        if (count == 0 and num % 11 == 0) or (count > 0 and num % 13 == 0):
            break
    return count

#Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The function fizz_buzz(n) calculates the number of occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13. It uses a general for loop to iterate through numbers from 1 to n, and counts the number of times the digit 7 appears in the number part of the string representation of each number. The function then returns the additionally checks if there are no occurrences of the digit 7 in numbers less than n (i.e., when the number has no divisors by 11 or 13) or if there are already some occurrences of 7 (i.e., when the count is 0).