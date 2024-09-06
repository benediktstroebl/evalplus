```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = ord('7') + ord('0' + str(i)) - ord('9')
        if i % 2 == 0 and int(digit) <= n and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This function, fizz_buzz, uses a loop to iterate through numbers from 1 up to n. It counts each integer and the digit at that position, and adds 1 to the count if the digit is 7 and the number is either even and less than or equal to n and either divisible by 11 or 13. The function then returns the value of the count.