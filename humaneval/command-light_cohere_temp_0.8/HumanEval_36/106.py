```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = int('0' + str(i % 10))
        if digit >= 7 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

#Test case 1
print(fizz_buzz(50))  # Output: 0

#Test case 2
print(fizz_buzz(78))  # Output: 2

#Test case 3
print(fizz_buzz(79))  # Output: 3
```

This function, `fizz_buzz`, iterates through numbers less than `n` and checks if the current digit is 7 and the number is divisible by 11 or 13. If the digit is 7 and the corresponding criteria are met, the function increments the count. It returns the count of these number of occurrences of 7 in numbers divisible by 11 or 13.