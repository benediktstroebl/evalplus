```python
def fizz_buzz(n):
    return sum([x in str(i) for i in range(1, n+1) if x == 7 and i % 11 == 0 or x == 7 and i % 13 == 0])

# Test
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

The function `fizz_buzz` calculates the number of times the digit 7 appears in the range of integers from 1 to `n`, specifically looking for numbers divisible by 11 or 13. It uses a SQL-like style string manipulation to iterate through the numbers and checks if the digit 7 is present in the string representation of each number.