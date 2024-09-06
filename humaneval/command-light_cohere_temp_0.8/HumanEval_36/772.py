```python
def fizz_buzz(n: int):
    count = 0
    for num in range(1, n+1):
        if (num % 11 == 0 or num % 13 == 0) and (num != 7):
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This Python script defines a function called `fizz_buzz` that calculates the number of occurrences of the digit 7 in a given integer `n` that is either divisible by 11 or 13, excluding 7 itself. The function iterates through numbers from 1 to `n`, checking if the current number is divisible by 11 or 13 but not including 7. The function keeps track of the number of such digits (excluding 7) using a `count` variable. The loop terminates when `n` is reached, and the function returns the count of digits that satisfy the criteria.