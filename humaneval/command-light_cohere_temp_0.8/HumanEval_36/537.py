Here is a self-contained Python script that defines a function fizz_buzz that solves the problem of counting the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    7 % 11 == 0 or 7 % 13 == 0
    return len({i for i in range(1, n+1) if i % 11 == 7 or i % 13 == 7})
```
This function efficiently uses list comprehension and modulus operators to count occurrences of 7 in numbers divisible by 11 or 13, less than n, and returns the result.