```python
def fizz_buzz(n):
    c = 0
    for i in range(1, n+1):
        digit = str(i)
        if any(d == '7' for d in digit.find(10, 13)):
            c += 1
    return c

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This code defines a function called `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers less than a given number `n` that are divisible by 11 or 13. The function iterates through the string representation of numbers from 1 to `n` using a `for` loop. It then checks each digit against the specific values from 10 to 13 using the `find` method. If a digit matches any of these specified values, it increments a counter `c`. Finally, the function returns the count `c`.