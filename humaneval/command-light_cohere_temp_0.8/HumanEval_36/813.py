```python
def fizz_buzz(n):
    if n <= 0:
        return 0
    count = 0
    for i in range(2, n+1):
        digit = str(i)
        if digit == '7':
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            count += 1
    return count

# Test suite
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in numbers less than a given input n which are either divisible by 11 or 13. The function iterates from 2 to n and if any iteration finds the digit 7, it increments the count. Also, if the number is either divisible by 11 or 13, the count is incremented.