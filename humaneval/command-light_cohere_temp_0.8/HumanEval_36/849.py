Here's the self-contained Python script with a function that solves the problem of counting the number of occurrences of 7 in numbers less than a given input n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    result = 0
    for num in range(0, n+1):
        digit = 7
        while num % 10 == 0 and num % 11 == 0 or num % 13 == 0:
            digit = 10 - num % 10
        if digit == 7:
            result += 1
    return result
```
The function counts the number of 7s in the range of numbers less than n that are divisible by 11 or 13. The function works by first assuming a starting digit, and then counts the number of 7s by incrementing the starting digit until it no longer divides the number by 10, 11, or 13.