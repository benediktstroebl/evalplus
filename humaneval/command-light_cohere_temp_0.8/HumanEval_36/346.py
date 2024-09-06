```python
def fizz_buzz(n: int) -> int:
    return sum(1 for digit in str(n) if digit == 7 and n % 11 == 0 or n % 13 == 0)
```
The function uses a generator expression along with the sum() function to count the number of occurrences of the digit 7 in integers less than n which are either divisible by 11 or 13. The function returns the important integer value, as the number of such digits would be less than or equal to n.