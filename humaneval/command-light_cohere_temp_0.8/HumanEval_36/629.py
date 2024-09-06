```python
def fizz_buzz(n):
    return sum([i in str(i) for i in range(1, n+1) if i % 11 == 7 or i % 13 == 7])

# Test the function
 assert fizz_buzz(50) == 0
 assert fizz_buzz(78) == 2
 assert fizz_buzz(79) == 3
```

This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in numbers less than n and divisible by 11 or 13. The function utilizes a `range` and `str` to generate all numbers from 1 to `n`, and checks if the digit 7 appears in the resulting string. The `sum` function is then used to count the occurrences of 7, returning the result.