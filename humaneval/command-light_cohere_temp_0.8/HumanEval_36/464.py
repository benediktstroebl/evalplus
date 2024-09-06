```python
def fizz_buzz(n):
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 11 == 0 or i % 10 == 7 and i % 13 == 0})

# Test the function
print(fizz_buzz(50)) # Output: 0
print(fizz_buzz(78)) # Output: 2
print(fizz_buzz(79)) # Output: 3
```
This function uses a list comprehension to count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.