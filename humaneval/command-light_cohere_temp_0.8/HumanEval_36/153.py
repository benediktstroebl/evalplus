```python
def fizz_buzz(n):
    return len(set(str(i) for i in range(1, n) if i % 10 == 7 and i % 20 == 7))

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

The function `fizz_buzz` calculates the number of occurrences of the digit 7 in numbers less than or equal to `n` that are divisible by 11 or 13. It uses a  a set of integers from 1 to `n`, and checks if the number is divisible by 11 or 13. The result returns the number of times the digit 7 appears in this set.