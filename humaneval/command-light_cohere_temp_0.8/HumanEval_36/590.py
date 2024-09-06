```python
def fizz_buzz(n: int):
    if n < 7:
        return 0
    i = 7
    while n >= i:
        if n % i == 0 or n % (i+4) == 0:
            if n % 11 == 0 or n % 13 == 0:
                return 1 + fizz_buzz(n // i)
            n //= i
        i += 4
    return 2

# Test the function with the provided inputs
assertEqual(fizz_buzz(50), 0)
assertEqual(fizz_buzz(78), 2)
assertEqual(fizz_buzz(79), 3)
```
This code defines a function `fizz_buzz` which calculates the number of occurrences of the number 7 in integers less than a given number n that are divisible by 11 or 13. The function uses a iterative approach with an initial value of 7, and then checks divisibility with increasing numbers until the input number, adjusting for both the original and the next closest number. The function then returns 2 if no such occurrences of 7 are found in this range.