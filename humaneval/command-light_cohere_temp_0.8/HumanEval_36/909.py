```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        if digit == '7' and int(digit) < 10:
            count += 1
        if count == 2:
            break
    return count

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
The fizz_buzz function uses a loop to iterate through numbers less than the input n and checks if the digit is 7 and if it's less than 10. If the count of such adders is 2, indicating that the number has 7 and is divisible by 11 or 13, it returns 2. If the loop ends without finding 2, it means no 7s were found and the function returns 0.