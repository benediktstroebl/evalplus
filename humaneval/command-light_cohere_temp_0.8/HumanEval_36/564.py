```python
def fizz_buzz(n: int):
    if n <= 0:
        return 0

    count = 0
    for i in range(2, n + 1):
        digit = str(i)
        while digit == '7':
            digit = str(next(i))
        count += (digit == '7') != True

    return count

# Example of testing the function
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
assert fizz_buzz(120) == 6
assert fizz_buzz(21) == 5
assert fizz_buzz(42) == 7
``` 
The function returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.