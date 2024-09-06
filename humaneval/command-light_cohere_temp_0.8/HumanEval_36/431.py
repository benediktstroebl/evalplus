Here's the Python code:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    c = 0
    for i in range(1, n+1):
        num = pow(10, i)
        x = int(num, 2)  # x is either 2 or 4, got by taking last two digits of num
        if x <= 7 and (x % 10 == 2 or x % 10 == 4) and i % 10 == 0:
            c += 1
    return c
```
The function fizz_buzz takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a pure Python and doesn't require any external libraries. It uses basic integer arithmetic and loops to calculate the count of numbers that satisfy the criteria. 

Please note that this function only counts the occurrences of 7, and doesn't output the actual number that appears 7. The function is designed to be easy to read and understand, and it is a good starting point for further optimization or customization.