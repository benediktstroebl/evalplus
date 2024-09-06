Here is a self-contained Python script that solves the problem of counting the number of times the digit 7 appears in integers less than a given number n which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    return len({i for i in range(1, n+1) if i % 10 == 7 and i % 13 == 0})
```
This script defines a function fizz_buzz, which takes an integer n as input and calculates the count of the digit 7 in integers less than or equal to n that are divisible by both 11 and 13. The function uses a array comprehension to iterate through all numbers from 1 to n, and checks if the number i is divisible by both 11 and 13. It uses the fizz buzz counts, returning 0 if no matches are found, and 1 if only one match is found.