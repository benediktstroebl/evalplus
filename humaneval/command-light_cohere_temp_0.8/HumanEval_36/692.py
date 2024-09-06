```python
def fizz_buzz(n: int):
    return 7 - (n // 13) if n % 13 != 0 else 0

# Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This code defines a function called **fizz_buzz** that calculates the number of times the digit 7 appears in the range from 0 to n, then less than n, in integers that are divisible by 13 or 11. The function works by keeping track of the 7-idgeting pattern as it moves through the numbers less than n. It returns 0 for n if no such 7 is found and returns the number of occurrences of 7 if it's present in the range.