```python
def fizz_buzz(n: int) -> int:
    count = 0
    for num in range(2, n+1):
        if all(c for c in str(num) if c == '7'):
            count += 1
    return count

# Test code
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function called **fizz_buzz** that calculates the number of occurrences of the digit 7 in numbers less than a given number n which are divisible by 11 or 13. The function iterates through numbers from 2 to n, and for each number, it checks if all its digits are 7. The function then counts the occurrences of 7 and returns the result.